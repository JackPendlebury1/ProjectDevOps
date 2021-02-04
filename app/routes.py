from flask import render_template, redirect, url_for, request
from app import app, db, bcrypt, login_manager
from app.models import *
from app.forms import *
from flask_login import login_required, logout_user, current_user, login_user



@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            getPerson = Users.query.filter_by(user_username=form.username.data).first()
            password = form.password.data
            if bcrypt.check_password_hash(getPerson.user_password, password):
                login_user(getPerson)
                return redirect(url_for('user_home'))
            else:
                return render_template("login.html", form=form ,message='not logged in')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            add_user = Users(
                user_first_name = form.first_name.data,
                user_last_name = form.last_name.data,
                user_username = form.username.data,
                user_password = bcrypt.generate_password_hash(form.password.data),
                user_email = form.email.data
            )
            db.session.add(add_user)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('register.html', form=form, message=form.errors)


@app.route('/user/home', methods=['GET'])
@login_required
def user_home():
    return render_template('user_home.html', current_user=current_user)


@app.route('/user/add_song', methods=['GET', 'POST'])
@login_required
def user_add_song():
    form = SongForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            add_song = Songs(
                song_name = form.name.data,
                song_artist = form.artist.data,
                song_genre = form.genre.data,
                song_release_date = form.release_date.data,
                song_length = form.length.data,
                owner_id = current_user.id
            )
            db.session.add(add_song)
            db.session.commit()
            return redirect(url_for('user_home'))

    return render_template('add_song.html', form=form, message=form.errors)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/user/update/song/<song_id>", methods=['GET', 'POST'])
@login_required
def update_song(song_id):
    song = Songs.query.filter_by(id=song_id).first()
    form = SongUpdateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            song.song_name = form.name.data,
            song.song_artist = form.artist.data,
            song.song_genre = form.genre.data,
            song.song_release_date = form.release_date.data,
            song.song_length = form.length.data,
            song.owner_id = current_user.id
            db.session.commit()
        return redirect(url_for('user_home'))
    return render_template('update_song.html', form=form, message=form.errors)

@app.route("/user/update/user/", methods=['GET', 'POST'])
@login_required
def update_user():
    user = Users.query.filter_by(id=current_user.id).first()
    form = UserUpdateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user.user_first_name = form.first_name.data,
            user.user_last_name = form.last_name.data,
            user.user_username = form.username.data,
            user.user_password = bcrypt.generate_password_hash(form.password.data),
            user.user_email = form.email.data
            db.session.commit()
        return redirect(url_for('user_home'))
    return render_template('update_user.html', form=form, message=form.errors)

@app.route("/user/delete/user/", methods=['GET', 'POST'])
@login_required
def delete_user():
    user = Users.query.filter_by(id=current_user.id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_home'))

@app.route("/user/delete/song/<song_id>", methods=['GET', 'POST'])
@login_required
def delete_song(song_id):
    song = Songs.query.filter_by(id=song_id).first()
    db.session.delete(song)
    db.session.commit()
    return redirect(url_for('user_home'))