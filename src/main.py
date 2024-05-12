import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from src.utils.api_client import APIClient
from src.utils.utils import int_list_to_str
from src.models.discover_movies_params import DiscoverMoviesParams
from src.utils.utils import flatten_dict

prompt = "I want to watch a movie similar to The Imitation Game so that I can be inspired."

# Tokenize the user prompt
tokens = word_tokenize(prompt)
print("Tokens:", tokens)

base_url = 'https://api.themoviedb.org/3'
api_client = APIClient(base_url)

# search movie
title = "The Imitation Game"
genre_ids = api_client.get_movie_genre_ids(title)
keywords = api_client.get_movie_keywords(title)

keyword_id_str = int_list_to_str(keywords, 'id')
genre_id_str = int_list_to_str(genre_ids)

params = DiscoverMoviesParams()
params.with_keywords = keyword_id_str
params.with_genres = genre_id_str

params = flatten_dict(params.__dict__)
recommended_movies = api_client.get_similar_movies(params)
print(recommended_movies)
