import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, nullable=False)
    age = sq.Column(sq.Integer)
    gender = sq.Column(sq.String(length=255))
    city = sq.Column(sq.String(length=255))

class FavoriteUsers(Base):
    __tablename__ = 'favorite_users'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False)
    name = sq.Column(sq.String(length=255), nullable=False)
    link = sq.Column(sq.String(length=255), nullable=False)

class Photos(Base):
    __tablename__ = 'photos'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False)
    photo_id = sq.Column(sq.Integer, nullable=False)
    photo_link = sq.Column(sq.String(length=255), nullable=False)
    likes = sq.Column(sq.Integer)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
