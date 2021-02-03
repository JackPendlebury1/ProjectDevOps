from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app import db
from app.models import Users

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(2,30)])
    password = StringField('Password', validators=[DataRequired(), Length(8,32)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(2,30)])
    password = StringField('Password', validators=[DataRequired(), Length(8,32)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(1,20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(1,50)])
    email = StringField('Email', validators=[DataRequired()])

    def validate_email(self, email):
            user = Users.query.filter_by(user_email=email.data).first()
            if user:
                raise ValidationError('This email is already registered do you have an account?')

    submit = SubmitField('Register')

class SongForm(FlaskForm):
    name = StringField('Song Name', validators=[DataRequired(), Length(2,50)])
    artist = StringField('Artist', validators=[DataRequired(), Length(2,50)])
    genre = StringField('Genre', validators=[DataRequired(), Length(2,50)])
    release_date = StringField('Release Date', validators=[DataRequired()])
    length = IntegerField('Song Length', validators=[DataRequired()])

    submit = SubmitField('Add Song')

class SongUpdateForm(FlaskForm):
    name = StringField('Song Name', validators=[DataRequired(), Length(2,50)])
    artist = StringField('Artist', validators=[DataRequired(), Length(2,50)])
    genre = StringField('Genre', validators=[DataRequired(), Length(2,50)])
    release_date = StringField('Release Date', validators=[DataRequired()])
    length = IntegerField('Song Length', validators=[DataRequired()])

    submit = SubmitField('Add Song')

class UserUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(2,30)])
    password = StringField('Password', validators=[DataRequired(), Length(8,32)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(1,20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(1,50)])
    email = StringField('Email', validators=[DataRequired()])

    def validate_email(self, email):
            user = Users.query.filter_by(user_email=email.data).first()
            if user:
                raise ValidationError('This email is already registered do you have an account?')

    submit = SubmitField('Register')