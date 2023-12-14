from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService:
    def __init__(self, db):
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category: str):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result

    def create_movie(self, movie: Movie) -> Movie:
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return new_movie

    def update_movie(self, id: int, movie: Movie) -> Movie:
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if result:
            result.title = movie.title
            result.overview = movie.overview
            result.year = movie.year
            result.rating = movie.rating
            result.category = movie.category
            self.db.commit()
            return result

    def delete_movie(self, id: int) -> Movie:
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if result:
            self.db.delete(result)
            self.db.commit()
            return result