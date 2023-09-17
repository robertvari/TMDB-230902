from typing import Optional
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
import tmdbsimple as tmdb
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole

    def __init__(self):
        super().__init__()
        self._movies = []

        self._fetch()
    
    def _fetch(self):
        pass

    def rowCount(self, parent=QModelIndex) -> int:
        return len(self._movies)
    
    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == MovieList.DataRole:
            return self._movies[row]
    
    def roleNames(self):
        return {MovieList.DataRole: b"data"}