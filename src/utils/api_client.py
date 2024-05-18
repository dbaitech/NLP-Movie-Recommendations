import requests
import os
from dotenv import load_dotenv

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = self.create_session()

    def create_session(self):
        load_dotenv()

        bearer_token = os.environ.get('BEARER_TOKEN')

        session = requests.Session()
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {bearer_token}'
        }
        session.headers.update(headers)
        return session

    def search_movie(self, title):
        url = f'{self.base_url}/search/movie'
        params = {'query': title, 'include_adult': False}
        response = self.session.get(url, params=params)
        if response.status_code // 100 == 2:
            search_results = response.json()['results']
            # return an object that holds the row attributes
            return search_results[0]
        else:
            raise Exception(f'Error {response.status_code}: {response.text}')

    def get_movie_keywords(self, movie_id):
        url = f'{self.base_url}/movie/{movie_id}/keywords'
        response = self.session.get(url)
        if response.status_code // 100 == 2:
            return response.json()['keywords']
        else:
            raise Exception(f'Error {response.status_code}: {response.text}')

    def get_movie_genre_ids(self, title):
        movie_info = self.search_movie(title)
        return movie_info['genre_ids']

    def get_movie_id(self, title):
        movie_info = self.search_movie(title)
        return movie_info['id']

    def get_keyword_id(self, keyword):
        url = f'{self.base_url}/search/keyword'
        params = {'query': keyword}
        response = self.session.get(url, params=params)
        if response.status_code // 100 == 2:
            search_results = response.json()['results']
            if search_results:
                # return an object that holds the row attributes
                return search_results[0]
            else:
                return None
        else:
            raise Exception(f'Error {response.status_code}: {response.text}')

    def get_similar_movies(self, movie_attributes: dict):
        url = f'{self.base_url}/discover/movie'
        params = {'include_adult': 'false', 'include_video': 'false', 'sort_by': 'popularity.desc'}
        params.update(movie_attributes)
        response = self.session.get(url, params=params)
        if response.status_code // 100 == 2:
            return response.json()['results']
        else:
            raise Exception(f'Error {response.status_code}: {response.text}')
