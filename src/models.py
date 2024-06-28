import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
  

class Planets(Base):
        __tablename__ = 'planets'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        population = Column(String(250), nullable=False)




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)




   




    class favourites_characters(Base):
        __tablename__ = 'favourite_characters'
        id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
        characters_relationship = Column(Integer, nullable=False)
        



        class favourites_planets(Base):
            __tablename__ = 'favourite_planets'
        id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
        planets_relationship = Column(Integer, nullable=False)



        class favourites_vehicles(Base):
            __tablename__ = 'favourite_vehicles'
        id = Column(Integer,ForeignKey('vehicles.id'), primary_key=True)
        vehicles_relationship = Column(Integer, nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
