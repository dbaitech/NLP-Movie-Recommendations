from .discover_movies_params import DiscoverMoviesParams


class Categories(DiscoverMoviesParams):
    def __init__(self):
        super().__init__()
        self.movie_title = None

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({'movie_title': self.movie_title})
        return base_dict