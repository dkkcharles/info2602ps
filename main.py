import json
from flask_cors import CORS
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, User, Post, UserReact 
from forms import LogIn, AddPost

''' Begin boilerplate code '''

''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''

def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  CORS(app)
  login_manager.init_app(app) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()

''' End Boilerplate Code '''

@app.route('/') #Reference lab 6 task 4
def index():
    form = LogIn()
    if form.validate_on_submit():
        data = request.form
        user = User.query.filter_by(username = data['username']).first()
        if user and user.check_password(data['password']): 
            flash('Logged in successfully.') 
            login_user(user) 
            return redirect(url_for('app')) 
        else:
            flash('Invalid username or password') 
            return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/app', methods=['GET', 'POST', 'DELETE']) #Reference lab 6 task 5
@login_required
def client_app():
    posts = Post.query.all()
    posts = [Post.toDict() for post in posts]
    if posts is None:
        posts = []

    #return json.dumps(posts)
    form = AddPost()
    if form.validate_on_submit():
        data = request.form
        post = Post(text=data[''], id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post Added!')
        return redirect(url_for('app'))

     
    return render_template('app.html',form=form,posts=posts)

    
def delete_todo(id):
  todo = Todo.query.filter_by(userid=current_identity.id, id=id).first()
  if todo == None:
    return 'Invalid id or unauthorized'
  db.session.delete(todo) # delete the object
  db.session.commit()
  return 'Deleted', 204

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
