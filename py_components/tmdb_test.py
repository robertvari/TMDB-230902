import tmdbsimple as tmdb
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"

def get_popular_movies(page):
    movies = tmdb.Movies()
    popular_movies = movies.popular(page=page)["results"]
    for i in popular_movies:
        title = i.get("title")
        release_date = i.get("release_date")
        vote_average = i.get("vote_average") * 10
        poster_path = None

    pass

get_popular_movies(2)