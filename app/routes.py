from flask import render_template, redirect, url_for, request
from app import app, db


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')