import media
import fresh_tomatoes
import httplib
import json

# set api key for calling themoviedb api
api_key = "14898796a3f8fad6e3fe91e7fd86ebd8"

# create connection to api and retrieve data through api call
conn = httplib.HTTPSConnection("api.themoviedb.org")
conn.request("GET", "/3/movie/top_rated?page=1"
             "&language=en-US&api_key={0}".format(api_key))
res = conn.getresponse()

movies = []

# process response message from api call, 200 => successful http response
if res.status == 200:

    # read response message and store data to movies_list
    data = res.read()
    loaded_data = json.loads(data)
    movies_list = loaded_data["results"]

    # iterate through each movie information and create Movie object
    for movie_info in movies_list:

        # retrieve video links for each movie through api
        conn.request("GET", "/3/movie/{0}/videos?language=en-US"
                     "&api_key={1}".format(movie_info["id"], api_key))
        res2 = conn.getresponse()
        data2 = res2.read()
        loaded_data2 = json.loads(data2)
        video_list = loaded_data2["results"]
        trailer = None

        # iterate through list of video links to find movie trailer
        for video in video_list:
            if video["type"] == "Trailer":
                trailer = "https://www.youtube.com/watch?v=" + video["key"]
                break
        # create Movie if trailer is found and save into movies list
        if trailer is not None:
            movie = media.Movie(movie_info["title"],
                                movie_info["overview"],
                                "https://image.tmdb.org/t/p/w600_and_h900_"
                                "bestv2/{0}".format(movie_info["poster_path"]),
                                trailer)
            movies.append(movie)

# parse movies to open_movies_page() in fresh_tomatoes class to create webpage
fresh_tomatoes.open_movies_page(movies)
