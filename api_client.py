import requests
import os
from dotenv import load_dotenv, dotenv_values

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

    def get_similar_movies(self, genres, keywords):
        url = f'{self.base_url}/discover/movie'
        params = {'include_adult': 'false', 'include_video': 'false', 'sort_by': 'popularity.desc',
                  'with_genres': genres, 'with_keywords': keywords}
        response = self.session.get(url, params=params)
        if response.status_code // 100 == 2:
            return response.json()['results']
        else:
            raise Exception(f'Error {response.status_code}: {response.text}')

    def make_request(self, endpoint, method='GET', params=None, data=None, headers=None):
        '''
        Make an HTTP request to the API.

        Args:
            endpoint (str): The API endpoint to call.
            method (str): The HTTP method to use (e.g., GET, POST, PUT, DELETE).
            params (dict, optional): Dictionary of URL parameters.
            data (dict, optional): Dictionary of data to send in the body of the request.
            headers (dict, optional): Dictionary of HTTP headers.

        Returns:
            dict: JSON response from the API.
        '''
        url = self.base_url + endpoint
        response = requests.request(method, url, params=params, data=data, headers=headers)

        # Check if the request was successful (status code 2XX)
        if response.status_code // 100 == 2:
            return response.json()
        else:
            # If the request was not successful, raise an exception
            raise Exception(f'Error {response.status_code}: {response.text}')

# Example usage:
# api_client = APIClient('https://api.example.com')
# response = api_client.make_request('/endpoint', method='GET', params={'param': 'value'})
# print(response)
