from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService():

    def __init__(self,db) -> None: #constructor
        self.db = db


    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    

    def get_category(self, id_category):
        result = self.db.query(MovieModel).filter(MovieModel.category == id_category).all()  
        return result

    def create_movie(self, movie:Movie):
        new_movie =MovieModel(**movie.dict())    #pasa los parametros
        self.db.add(new_movie) 
        self.db.commit()               #ingresa el modelos 
        return 
    
    def update_movie(self, id:int, data :Movie):
        resul = self.db.query(MovieModel).filter(MovieModel.id == id ).first()               #hace la consulta por categoria verfica la existencia  
        resul.title=data.title                                                         #actualiza
        resul.overview=data.overview
        resul.year=data.year
        resul.rating=data.rating
        resul.category=data.category
        self.db.commit()       #ingresa el modelos 
        return 
    def delte_movie(self, id):
        self.db.query(MovieModel).filter(MovieModel.id == id ).delete(id)
        self.db.commit() 
        return 