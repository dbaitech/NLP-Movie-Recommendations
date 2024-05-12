import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from src.utils.api_client import APIClient
from src.utils.utils import int_list_to_str

# prompt = "I want to watch a movie similar to The Imitation Game so that I can be inspired and be in love with math again."

# Tokenize the user prompt
# tokens = word_tokenize(prompt)
#
# # Display the tokens
# print("Tokens:", tokens)

base_url = 'https://api.themoviedb.org/3'
api_client = APIClient(base_url)

# search movie
title = "The Imitation Game"
genre_ids = api_client.get_movie_genre_ids(title)
keywords = api_client.get_movie_keywords(title)
print("genres: ", genre_ids)
print("keywords: ", keywords)
keyword_id_str = int_list_to_str(keywords, 'id')
genre_id_str = int_list_to_str(genre_ids)
print(keyword_id_str, genre_id_str)