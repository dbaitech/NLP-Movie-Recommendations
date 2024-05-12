from discover_movies_params import DiscoverMoviesParams


class ParseCategories(DiscoverMoviesParams):
    def __init__(self):
        super().__init__()
        self.movie_title = None
