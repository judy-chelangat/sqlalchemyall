from sqlalchemy import (create_engine,Column,Integer,String,Sequence,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker,relationship

# define the database connection 
DATABASE_URI = 'sqlite:///movies.db' #path to the database
engine = create_engine(DATABASE_URI, echo=True)
 #creating the engine

#base class for allthe classes
Base = declarative_base() 


class Director(Base):
    __tablename__='director'
    dir_id =Column(Integer, Sequence('dir_id_seq'),primary_key=True)
    dir_name=Column(String)
    dir_experience=Column(Integer)

    movie = relationship('Movie', back_populates='director')



class Movie(Base):
    __tablename__='movie'
    movie_id = Column(Integer,Sequence('movie_id_seq'),primary_key=True)
    movie_title=Column(String)
    movie_plot=Column(String)
    movie_genre=Column(String)
    director_id = Column(Integer,ForeignKey('director.dir_id'))

    director = relationship('Director', back_populates='movie') #one to one relationship
    movie_cast= relationship('Cast',back_populates='movies')


class Actor(Base):
    __tablename__='actor'
    actor_id = Column(Integer,Sequence('actor_id_seq'),primary_key=True)
    actor_name=Column(String(255))
    actor_gender=Column(String(255))
    actor_salary=Column(Integer)
   
    cast = relationship('Cast',back_populates='actors')

class Cast(Base):
    __tablename__='cast'
    cast_id = Column(Integer,Sequence('cast_id_seq'),primary_key=True)
    actor_id=Column(Integer,ForeignKey('actor.actor_id'))
    movie_id=Column(Integer,ForeignKey('movie.movie_id'))
    
    actors = relationship('Actor', back_populates='cast')
    movies = relationship('Movie',back_populates='movie_cast')
#creating all the tables 
Base.metadata.create_all(bind=engine)

#create session
Session = sessionmaker(bind=engine)
session = Session()


#inserting data into the databse
#creating the instances

#