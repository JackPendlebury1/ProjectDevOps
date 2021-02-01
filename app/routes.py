from flask import render_template, redirect, url_for, request
from app import app, db, bcrypt
from app.models import *
from app.forms import *


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
                return redirect(url_for('home'))
            else:
                return render_template("login.html",form=form ,message='not logged in')
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