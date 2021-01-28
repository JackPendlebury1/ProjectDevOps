from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(15))
    user_last_name = db.Column(db.String(20))
    user_username = db.Column(db.String(15))
    user_password = db.Column(db.String(32))
    user_email = db.Column(db.String(60))