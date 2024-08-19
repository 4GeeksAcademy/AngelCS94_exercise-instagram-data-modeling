import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base): 
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)  
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(40), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'

    user_from_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    user_from_idRelationship = relationship(User)
    user_to_id = Column(String,ForeignKey('user.id')) 
    user_to_idRelationship = relationship(User)


class Post(Base):
    __tablename__='post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    user_idRelationship = relationship(User) 

class Comment(Base):
    __tablename__='comment'

    id = Column(Integer, primary_key=True)
    coment_text = Column(String(180))
    author_id = Column(Integer, ForeignKey('user.id'))
    author_idRelationship = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_idRelationship = relationship(Post)

class Media(Base):
    __tablename__='media'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_idRelationship = relationship(Post)

     






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
