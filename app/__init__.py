from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__,template_folder='../templates')
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE')
app.config['SECRET_KEY'] = os.environ.get('SECRET')

db = SQLAlchemy(app)

from app import routes