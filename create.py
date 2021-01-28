from app import db, models
from decouple import config

db.drop_all()
db.create_all()