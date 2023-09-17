from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import os, sys
from py_components.resources import Resources
from py_components.movie_list import MovieList

APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")


class TMDB:
    def __init__(self):
        # instance of QGuiApplication
        self.app = QGuiApplication(sys.argv)

        # instace of Qml Engine
        self.engine = QQmlApplicationEngine()

        # get a reference to QML context
        self.context = self.engine.rootContext()

        # Resource loader
        self.resources = Resources()
        self.context.setContextProperty("Resources", self.resources)

        # MovieList model
        self.movie_list = MovieList()
        self.context.setContextProperty("MovieList", self.movie_list)

        # load main.qml
        self.engine.load(MAIN_QML)

        if not self.engine.rootObjects():
            sys.exit(-1)

        sys.exit(self.app.exec())

if __name__ == "__main__":
    TMDB()