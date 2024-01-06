from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route('/where_to_begin')
def where_to_begin():
    return render_template('where_to_begin.html', title='С чего начать?')


@app.route('/folk')
def folk():
    return render_template('folk.html', title='Фолклер')