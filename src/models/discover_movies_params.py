class DiscoverMoviesParams:
    def __init__(self):
        self.primary_release_year = None
        self.primary_release_date.gte = None
        self.primary_release_date.lte = None
        self.region = None
        self.with_cast = None
        self.with_companies = None
        self.with_crew = None
        self.with_genres = None
        self.with_keywords = None
        self.with_origin_country = None
        self.with_original_language = None
        self.with_people = None
        self.with_runtime.gte = None
        self.with_runtime.lte = None
        self.without_companies = None
        self.without_genres = None
        self.without_keywords = None