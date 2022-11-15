class Tag:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp