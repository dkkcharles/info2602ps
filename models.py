from flask_sqlalchemy import SQLAlchemy
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

class UserReact(db.Model):
    id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    postid = db.Column('postid', db.Integer, db.ForeignKey('post.postid'))
    react = db.Column(db.String('like'|'dislike')


class Post(db.Model):
    postid = db.Column(db.Integer, primary_key =True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'),)
    text = db.column(db.String(280), nullable=False)
    reacts = db.relationship('UserReact')

    def getTotalLikes():
        return{
            total
        }
    
    def getTotalDislikes():
        return{
            total
        }

    def toDict(self):
        return{
            "User" : self.user.username,
            "Likes" : self.getTotalLikes,
            "Dislikes" : self.getTotalDislikes
        }