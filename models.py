from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
            }
    
    def set_password(self,password):
        self.password = generate_password_hash(password,method='sha256')

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    postid = db.Column(db.Integer, primary_key =True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    text = db.Column(db.String(280), nullable=False)
    reacts = db.relationship('UserReact')

    def getTotalLikes(self):
        j=0
        for react in self.reacts:
            if react.react == 'Like':
                j=j+1
        return j
    
    def getTotalDislikes():
        j=0
        for react in self.reacts:
            if react.react == 'Dislike':
                j=j+1
        return j

    def toDict(self):
        return{
            "Text" : self.text,
            "User" : self.user.username,
            "Likes" : self.getTotalLikes(),
            "Dislikes" : self.getTotalDislikes()
        }

class UserReact(db.Model):
    urid = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    postid = db.Column('postid', db.Integer, db.ForeignKey('post.postid'))
    react = db.Column(db.String(7))
