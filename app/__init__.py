from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

app = Flask(__name__,template_folder='../templates')


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE')
app.config['SECRET_KEY'] = 'THISISNOTASECRETANYMORE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes