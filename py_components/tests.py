import tmdbsimple as tmdb
import resources
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

BACKDROP_URL = f"https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"

movie = tmdb.Movies(278)
movie_data = movie.info()
backdrop_url = movie_data.get("backdrop_path")

print(resources.get_image_from_url(f"{BACKDROP_URL}{backdrop_url}"))