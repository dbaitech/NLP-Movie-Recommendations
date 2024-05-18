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
openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_prompt_categories(prompt):
    categories = Categories().to_dict()
    # llm = Llama(model_path="./models/7B/llama-model.gguf")
    # response = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"Extract the categories from the following text and assign them into the JSON object's "
                        f"categories. Be careful to place any movie titles in the appropriate category, not just "
                        f"in with_keywords. Return only the given JSON object with filled in values."
                        f"{prompt}\n\n"
                        f"Categories: {categories}\n\n"},
        ]
    )
    return response


prompt = "I want to watch a movie similar to The Imitation Game so that I can be inspired."
ai_response = get_prompt_categories(prompt)
content = json.loads(ai_response.choices[0].message.content)
categories = content['categories']

base_url = 'https://api.themoviedb.org/3'
api_client = APIClient(base_url)

similar_movie_genre_id_str = []
similar_movie_keyword_id_str = []
# search movie if mentioned by user
if categories['movie_title']:
    title = categories['movie_title']
    similar_movie = MovieSearchResult(**api_client.search_movie(title))

    similar_movie_genre_ids = similar_movie.genre_ids
    similar_movie_keywords = api_client.get_movie_keywords(similar_movie.id)

    similar_movie_genre_id_str = int_list_to_str(similar_movie_genre_ids)
    similar_movie_keyword_id_str = int_list_to_str(similar_movie_keywords, 'id')


params = DiscoverMoviesParams()
params.with_genres += similar_movie_genre_id_str
params.with_keywords += similar_movie_keyword_id_str

params = flatten_dict(params.__dict__)
recommended_movies = api_client.get_similar_movies(params)
print(recommended_movies)
