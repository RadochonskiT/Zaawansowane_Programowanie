class Rating:
    def __init__(self, userId: int, movieId: int, rating: int, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp