from src.utils.utils import flatten_dict


class DiscoverMoviesParams():
    def __init__(self):
        super().__init__()
        self.primary_release_year = None
        self.primary_release_date = {'gte': None, 'lte': None}
        self.region = None
        self.with_cast = None
        self.with_companies = None
        self.with_crew = None
        self.with_genres = None
        self.with_keywords = None
        self.with_origin_country = None
        self.with_original_language = None
        self.with_people = None
        self.with_runtime = {'gte': None, 'lte': None}
        self.without_companies = None
        self.without_genres = None
        self.without_keywords = None

    def to_dict(self):
        return {
            'primary_release_year': self.primary_release_year,
            'primary_release_date': self.primary_release_date,
            'region': self.region,
            'with_cast': self.with_cast,
            'with_companies': self.with_companies,
            'with_crew': self.with_crew,
            'with_genres': self.with_genres,
            'with_keywords': self.with_keywords,
            'with_origin_country': self.with_origin_country,
            'with_original_language': self.with_original_language,
            'with_people': self.with_people,
            'with_runtime': self.with_runtime,
            'without_companies': self.without_companies,
            'without_genres': self.without_genres,
            'without_keywords': self.without_keywords
        }