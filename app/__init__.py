from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE')

db = SQLAlchemy(app)

from app import routes