import tmdbsimple as tmdb
from resources import get_image_from_url
from datetime import datetime
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"

movie_list = []

movies = tmdb.Movies()
for page in range(1, 10):
    popular_movies = movies.popular(page=page)["results"]

    for i in popular_movies:
        title = i.get("title")
        release_date = datetime.strptime(i.get("release_date"), "%Y-%m-%d")
        vote_average = i.get("vote_average") * 10
        poster_path = get_image_from_url(f"{POSTER_ROOT_PATH}{i.get('poster_path')}")
        id = i.get("id")

        movie_list.append({
            "id": i.get("id"),
            "title": title,
            "display_date": release_date.strftime("%Y %B %d"),
            "sort_date": release_date,
            "vote_average": vote_average,
            "poster_path": poster_path
        })