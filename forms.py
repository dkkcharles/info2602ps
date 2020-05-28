from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Email

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class AddPost(FlaskForm):
  text = TextAreaField('Text', validators =[InputRequired()])
  submit = SubmitField('Add Post', render_kw={'class': 'btn waves-effect waves-light white-text'})
