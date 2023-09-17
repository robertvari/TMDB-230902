from typing import Optional
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, QObject, QRunnable, Signal, QThreadPool
from py_components.resources import get_image_from_url
import tmdbsimple as tmdb
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole

    def __init__(self):
        super().__init__()
        self._movies = []

        self._job_pool = QThreadPool()
        self._job_pool.setMaxThreadCount(1)
        self._movie_list_worker = MovieListWorker()

        self._fetch()
    
    def _fetch(self):
        self._movie_list_worker.signals.task_finished.connect(self._insert_movie)
        self._job_pool.start(self._movie_list_worker)

    def _insert_movie(self, movie_data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._movies.append(movie_data)
        self.endInsertRows()

    def rowCount(self, parent=QModelIndex) -> int:
        return len(self._movies)
    
    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == MovieList.DataRole:
            return self._movies[row]
    
    def roleNames(self):
        return {MovieList.DataRole: b"movie_data"}
    

class WorkerSignals(QObject):
    task_finished = Signal(dict)

    def __init__(self):
        super().__init__()


class MovieListWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        self.movies = tmdb.Movies()

    def run(self):
        self._fetch()

    def _fetch(self):
        popular_movies = self.movies.popular(page=1)["results"]
        for i in popular_movies:
            title = i.get("title")
            release_date = i.get("release_date")
            vote_average = i.get("vote_average") * 10
            poster_path = get_image_from_url(f"{POSTER_ROOT_PATH}{i.get('poster_path')}")

            self.signals.task_finished.emit({
                "title": title,
                "release_date": release_date,
                "vote_average": vote_average,
                "poster_path": poster_path
            })