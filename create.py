from app import db, models
from decouple import config

print(config('DATABASE'))
db.drop_all()
db.create_all()