class MovieSearchResult:
    def __init__(self, **kwargs):
        self.backdrop_path = kwargs.get('backdrop_path', None)
        self.genre_ids = kwargs.get('genre_ids', None)
        self.id = kwargs.get('id', None)
        self.original_language = kwargs.get('original_language', None)
        self.original_title = kwargs.get('original_title', None)
        self.overview = kwargs.get('overview', None)
        self.popularity = kwargs.get('popularity', None)
        self.poster_path = kwargs.get('poster_path', None)
        self.release_date = kwargs.get('release_date', None)
        self.title = kwargs.get('title', None)
