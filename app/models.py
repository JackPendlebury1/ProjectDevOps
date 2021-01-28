from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(15))
    user_last_name = db.Column(db.String(20))
    user_username = db.Column(db.String(15))
    user_password = db.Column(db.String(32))
    user_email = db.Column(db.String(60))

    songs = db.relationship("Songs", back_populates="owner")


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(50))
    song_artist = db.Column(db.String(20))
    song_genre = db.Column(db.String(15))
    song_release_date = db.Column(db.String(32))
    song_length = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    owner = db.relationship("Users", back_populates="songs")