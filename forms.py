from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
   
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

#     - pip install Flask-WTF
# - pip install Flask-Migrate
# - pip install psycopg2
# - pip install psycopg2-binary -- For those on mac machines
# - pip install email-validator -- Verification of emails inside of forms
# - pip install python-dotenv
