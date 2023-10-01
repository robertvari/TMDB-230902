import tmdbsimple as tmdb
from py_components.resources import get_image_from_url
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

movie = tmdb.Movies(278)
movie_data = movie.info()
backdrop_url = movie_data.get("backdrop_path")

