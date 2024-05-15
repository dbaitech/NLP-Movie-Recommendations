import json
import os

import spacy
from src.models.categories import Categories
from src.utils.api_client import APIClient
from src.utils.utils import int_list_to_str
from src.models.discover_movies_params import DiscoverMoviesParams
from src.models.movie_search_result import MovieSearchResult
from src.utils.utils import flatten_dict
from openai import OpenAI
from dotenv import load_dotenv
from llama_cpp import Llama

load_dotenv()
# openai_client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )
def get_prompt_categories(prompt):
    categories = Categories().to_dict()
    llm = Llama(model_path="./models/7B/llama-model.gguf")
    response = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
    # response = openai_client.completions.create(
    #     model="gpt-3.5-turbo",
    #     prompt=f"Extract the categories from the text and assign them into the JSON object's categories: {prompt}\n\n"
    #            f"Categories: {categories}\n\n",
    # )
    return response

prompt = "I want to watch a movie similar to The Imitation Game so that I can be inspired."
ai_response = get_prompt_categories(prompt)
print(ai_response)
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(prompt)
# # relevant_tokens = []
# for token in doc:
#     print(token.ent_type_)
#     if token.pos_ in ['NOUN', 'PROPN'] or token.ent_type_ == 'DATE':
#         relevant_tokens.append(token.text)
#
# print("Relevant tokens:", relevant_tokens)

base_url = 'https://api.themoviedb.org/3'
api_client = APIClient(base_url)

# search movie
title = "The Imitation Game"
movie = MovieSearchResult(**api_client.search_movie(title))

genre_ids = movie.genre_ids
keywords = api_client.get_movie_keywords(movie.id)

keyword_id_str = int_list_to_str(keywords, 'id')
genre_id_str = int_list_to_str(genre_ids)

params = DiscoverMoviesParams()
params.with_keywords = keyword_id_str
params.with_genres = genre_id_str

params = flatten_dict(params.__dict__)
recommended_movies = api_client.get_similar_movies(params)
print(recommended_movies)
