from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
import os


app = Flask(__name__,template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE')

db = SQLAlchemy(app)

from app import routes