from typing import Optional

from PySide6.QtCore import (
    QAbstractListModel, 
    QModelIndex, 
    Qt, 
    QObject, 
    QRunnable, 
    Signal, 
    QThreadPool, 
    Property, 
    QSortFilterProxyModel,
    Slot
)

from py_components.resources import get_image_from_url
import tmdbsimple as tmdb
from datetime import datetime

tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole
    download_progress_changed = Signal()

    def __init__(self):
        super().__init__()
        self._movies = []

        self._job_pool = QThreadPool()
        self._job_pool.setMaxThreadCount(1)
        self._movie_list_worker = MovieListWorker(max_pages=10)

        self._fetch()
    
    @property
    def movies(self):
        return self._movies

    def _fetch(self):
        self.download_progress_changed.emit()

        self._movie_list_worker.signals.task_finished.connect(self._insert_movie)
        self._job_pool.start(self._movie_list_worker)

    def _insert_movie(self, movie_data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._movies.append(movie_data)
        self.endInsertRows()

        self.download_progress_changed.emit()

    def rowCount(self, parent=QModelIndex) -> int:
        return len(self._movies)
    
    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == MovieList.DataRole:
            return self._movies[row]
    
    def roleNames(self):
        return {MovieList.DataRole: b"movie_data"}
    
    def _get_is_downloading(self):
        return self._movie_list_worker.working

    def _get_download_current_value(self):
        return self._movie_list_worker.current_count
    
    def _get_download_max_count(self):
        return self._movie_list_worker.max_pages * 20

    def _get_genres(self):
        return self._movie_list_worker.genres

    is_downloading = Property(bool, _get_is_downloading, notify=download_progress_changed)
    download_current_value = Property(int, _get_download_current_value, notify=download_progress_changed)
    download_max_count = Property(int, _get_download_max_count, notify=download_progress_changed)
    genres = Property(list, _get_genres, constant=True)

class MovieListProxy(QSortFilterProxyModel):
    genre_changed = Signal()
    sorting_changed = Signal()

    def __init__(self):
        super().__init__()
        self.sort(0, Qt.AscendingOrder)

        self._title_filter = ""
        self._genre = None
        self._sorting_options = ["Rating Descending", "Rating Ascending", "Release Date Descending", "Release Date Ascending", "Title (A-Z)", "Title (Z-A)"]
        self._current_sorting = self._sorting_options[0]

    @Slot(str)
    def set_search(self, search_string):        
        self._title_filter = search_string
        self.invalidateFilter()



    def filterAcceptsRow(self, source_row, source_parent):
        moive_data = self.sourceModel().movies[source_row]
        result = True
        
        # filter out by title
        if self._title_filter.lower() not in moive_data.get("title").lower():
            result = False

        # filter out by genre
        if self._genre and self._genre not in moive_data.get("genres"):
            result = False

        return result

    def lessThan(self, source_left, source_right):
        left_movie = self.sourceModel().data(source_left, Qt.UserRole)
        right_movie = self.sourceModel().data(source_right, Qt.UserRole)
        
        if self._current_sorting == self._sorting_options[0]:
            return left_movie["vote_average"] > right_movie["vote_average"]
        elif self._current_sorting == self._sorting_options[1]:
            return left_movie["vote_average"] < right_movie["vote_average"]
        elif self._current_sorting == self._sorting_options[2]:
            return left_movie["sort_date"] > right_movie["sort_date"]
        elif self._current_sorting == self._sorting_options[3]:
            return left_movie["sort_date"] < right_movie["sort_date"]
        elif self._current_sorting == self._sorting_options[4]:
            return left_movie["title"] < right_movie["title"]
        elif self._current_sorting == self._sorting_options[5]:
            return left_movie["title"] > right_movie["title"]

    def _get_current_genre(self):
        return self._genre
    
    def _set_current_genre(self, new_genre):
        if new_genre == self._genre:
            self._genre = None
        else:
            self._genre = new_genre
        
        self.invalidateFilter()
        self.genre_changed.emit()

    def _get_sorting_options(self):
        return self._sorting_options

    def _get_current_sorting(self):
        return self._current_sorting
    
    def _set_current_sorting(self, new_sorting):
        self._current_sorting = new_sorting
        self.sorting_changed.emit()
        self.invalidate()

    current_genre = Property(str, _get_current_genre, _set_current_genre, notify=genre_changed)
    sorting_options = Property(list, _get_sorting_options, constant=True)
    current_sorting = Property(str, _get_current_sorting, _set_current_sorting, notify=sorting_changed)


class WorkerSignals(QObject):
    task_finished = Signal(dict)

    def __init__(self):
        super().__init__()


class MovieListWorker(QRunnable):
    def __init__(self, max_pages):
        super().__init__()
        self.signals = WorkerSignals()
        self.movies = tmdb.Movies()
        self.working = False
        self.current_count = 0
        self.max_pages = max_pages

        self._movie_genres = {}
        for i in tmdb.Genres().movie_list()["genres"]:
            self._movie_genres[i.get("id")] = i.get("name")
    
    @property
    def genres(self):
        return list(self._movie_genres.values())

    def run(self):
        self.current_count = 0
        self.working = True
        self._fetch()
        self.working = False

    def _get_genres(self, genre_id_list) -> list:
        if not genre_id_list:
            return []

        return [self._movie_genres[i] for i in genre_id_list]

    def _fetch(self):
        def slice_long_text(text, max_length):
            if len(text) > max_length:
                return f"{text[:max_length]}..."
            return text


        for page in range(1, self.max_pages+1):
            popular_movies = self.movies.popular(page=page)["results"]

            for i in popular_movies:
                title = slice_long_text(i.get("title"), 40)
                release_date = datetime.strptime(i.get("release_date"), "%Y-%m-%d")
                vote_average = i.get("vote_average") * 10
                poster_path = get_image_from_url(f"{POSTER_ROOT_PATH}{i.get('poster_path')}")

                self.current_count += 1
                self.signals.task_finished.emit({
                    "title": title,
                    "display_date": release_date.strftime("%Y %B %d"),
                    "sort_date": release_date,
                    "vote_average": vote_average,
                    "poster_path": poster_path,
                    "genres": self._get_genres(i.get("genre_ids"))
                })