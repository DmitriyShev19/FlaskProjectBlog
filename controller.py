from werkzeug.security import generate_password_hash

from app import app
from flask import render_template, request, redirect, url_for

from models import User


@app.route('/')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    login = request.form.get('login', '_')
    email = request.form.get('email')
    password = request.form.get('password')
    if check_new_user(login=login, email=email, password=password):
        forms = dict(request.form)
        forms['password'] = generate_password_hash(password)
        User.create(**forms)
        return redirect(url_for('input_user'))
    return render_template('register.html')




@app.route('/where_to_begin')
def where_to_begin():
    return render_template('where_to_begin.html', title='С чего начать?')


@app.route('/folk')
def folk():
    return render_template('folk.html', title='Фолклер')