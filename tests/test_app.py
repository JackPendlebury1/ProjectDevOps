import unittest
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from app import app, db, bcrypt
from app.models import Users, Songs

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                DEBUG=True,
                WTF_CSRF_ENABLED = False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.session.commit()
        db.drop_all()
        db.create_all()

        self.app.config['LOGIN_DISABLED'] = True

        # Create test user
        user = Users(
                    user_first_name = "John",
                    user_last_name = "Doe",
                    user_username = "Johnny102",
                    user_password = bcrypt.generate_password_hash("bigJohnny123"),
                    user_email = "johnny123@gmail.com"
                )

        song = Songs(
                song_name = "a good song name",
                song_artist = "a good artist name",
                song_genre = "a good genre name",
                song_release_date = "2020-09-01",
                song_length = 90,
                owner_id = user.id
            )

        # save song to database
        db.session.add(song)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code,200)

    def test_register_get(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code,200)
    

class TestLoggedinViews(TestBase):

    def test_register_post(self):
            response = self.client.post(url_for("register"),data = dict(user_first_name = "john",
                user_last_name = "john",
                user_username = "johnny21321321",
                user_password = bcrypt.generate_password_hash("12345687"),
                user_email = "johnn@gmail.com"),follow_redirects = True)
            self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post(url_for("login"),data = dict(username = "Johnny102", password = "bigJohnny123"),follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_user_home_post(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
        response = self.client.get(url_for('user_home'),follow_redirects = True)
        self.assertEqual(response.status_code,200)

    def test_add_song_post(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
        response = self.client.post(url_for('user_add_song'),data = dict(song_name = "song",
                song_artist = "song",
                song_genre = "song",
                song_release_date = "song",
                song_length = 90,
                owner_id = 1), follow_redirects = True)
        self.assertEqual(response.status_code,200)

    def test_update_song_post(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
            response = self.client.post(url_for('update_song', song_id = 1), data = dict(song_name = "song",
                song_artist = "song",
                song_genre = "song",
                song_release_date = "song",
                song_length = 90,
                owner_id = 1), follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_update_user_post(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
            self.client.get(url_for("update_user", user_id = 1), follow_redirects = True)
        response = self.client.post(url_for('update_user', user_id = 1), data = dict(user_first_name = "John",
                    user_last_name = "Doe",
                    user_username = "Johnny102",
                    user_password = bcrypt.generate_password_hash("bigJohnny123"),
                    user_email = "johnny123111@gmail.com"
                ),follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_song(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
            self.client.post(url_for('user_add_song'),data = dict(song_name = "song",
                song_artist = "song",
                song_genre = "song",
                song_release_date = "song",
                song_length = 90,
                owner_id = 1), follow_redirects = True)
        response = self.client.post(url_for('delete_song', song_id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
        response = self.client.post(url_for('delete_user', user_id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestLogout(TestBase):

    def test_logout_post(self):
        with self.client:
            self.client.post(url_for("login"),data = dict(username = "Johnny102",password = "bigJohnny123"),follow_redirects = True)
        response = self.client.get(url_for("logout"),follow_redirects = True)
        self.assertEqual(response.status_code, 200)