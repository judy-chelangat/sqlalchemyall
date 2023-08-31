from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Director, Movie, Actor, Cast  # Import the necessary classes
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# define the database connection 
DATABASE_URI = 'sqlite:///movies.db' #path to the database
engine = create_engine(DATABASE_URI, echo=True)
 #creating the engine


#create session
Session = sessionmaker(bind=engine)
session = Session()
session.query(Director).delete()
session.query(Actor).delete()
session.query(Cast).delete()

#director
dir1=Director(dir_name='zack snyder',dir_experience=10)
dir2=Director(dir_name='george',dir_experience=3)

#adding the instances 
session.add_all([dir1,dir2])
session.commit()

#actors
actor1=Actor(actor_name='judy',actor_gender='female',actor_salary=600000)
actor2=Actor(actor_name='maingi',actor_gender='male',actor_salary=500000)
actor3=Actor(actor_name='hakim',actor_gender='male',actor_salary=400000)

session.add_all([actor1,actor2,actor3])
session.commit()

#movie
movie1= Movie(movie_title='justin league',movie_plot='hjhjhjhjhhj',movie_genre='action',director_id=dir1.dir_id)

session.add(movie1)
session.commit()

#cast
cast1 = Cast(actor_id =actor1.actor_id ,movie_id = movie1.movie_id)
cast2 = Cast(actor_id =actor2.actor_id ,movie_id = movie1.movie_id)

session.add_all([cast1,cast2])
session.commit()


#getting the data
all_actors= session.query(Actor).all()

for actor in all_actors:
    print (actor.actor_name)

#get a movie
one_movie = session.query(Movie).filter_by(movie_id =1).first()
print(one_movie.movie_title)

#getting the director using the relationship
#print(one_movie.director.dir_name)
# print(all_actors) #it wil come as a list of objects 
session.close()

