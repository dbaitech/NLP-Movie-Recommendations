from .discover_movies_params import DiscoverMoviesParams


class Categories(DiscoverMoviesParams):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        delattr(self, "with_genres")
        self.movie_title = kwargs.get('movie_title', None)

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({'movie_title': self.movie_title})
        return base_dict