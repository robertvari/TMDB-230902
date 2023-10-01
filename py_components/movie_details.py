from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl
import tmdbsimple as tmdb
from py_components.resources import get_image_from_url
from datetime import datetime, timedelta

class MovieDetails(QObject):
    movie_changed = Signal()

    def __init__(self):
        super().__init__()
        self._movie_data = None

    @Slot(int)
    def set_movie(self, movie_id):
        movie = tmdb.Movies(movie_id)
        self._movie_data = movie.info()
        self.movie_changed.emit()

    def _get_title(self):
        if not self._movie_data:
            return ""
        title = self._movie_data.get("title")
        year = datetime.strptime(self._movie_data.get("release_date"), "%Y-%m-%d").year
        return f"{title} ({year})"

    def _get_overview(self):
        return self._movie_data.get("overview") if self._movie_data else ""
    
    def _get_tagline(self):
        return self._movie_data.get("tagline") if self._movie_data else ""
    
    def _get_genres(self):
        if not self._movie_data:
            return ""
        
        genres = [i["name"] for i in self._movie_data.get("genres")]
        return ", ".join(genres) if self._movie_data else ""
    
    def _get_poster(self):
        return get_image_from_url(self._movie_data.get("poster_path")) if self._movie_data else ""
    
    def _get_release_date(self):
        if not self._movie_data:
            return ""
        
        release_date = datetime.strptime(self._movie_data.get("release_date"), "%Y-%m-%d")
        return release_date.strftime("%Y %B %d")
    
    def _get_runtime(self):
        if not self._movie_data:
            return ""
        
        t_delta = timedelta(seconds=self._movie_data.get("runtime"))
        d, h, m = str(t_delta).split(":")

        return f"{int(h)}h {int(m)}m"
    
    def _get_vote_average(self):
        return 60
    
    def _get_backdrop(self):
        if not self._movie_data:
            return ""
        backdrop_url = self._movie_data.get("backdrop_path")
        backdrop_server_path = f"https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
        return get_image_from_url(f"{backdrop_server_path}{backdrop_url}")

    title = Property(str, _get_title, notify=movie_changed)
    overview = Property(str, _get_overview, notify=movie_changed)
    tagline = Property(str, _get_tagline, notify=movie_changed)
    genres = Property(str, _get_genres, notify=movie_changed)
    poster = Property(QUrl, _get_poster, notify=movie_changed)
    release_date = Property(str, _get_release_date, notify=movie_changed)
    runtime = Property(str, _get_runtime, notify=movie_changed)
    vote_average = Property(int, _get_vote_average, notify=movie_changed)
    backdrop = Property(QUrl, _get_backdrop, notify=movie_changed)