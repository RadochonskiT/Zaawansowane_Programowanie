class Movie:
    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres

    def __str__(self) -> str:
        return f'Movie {self.title} is a {self.genres}'