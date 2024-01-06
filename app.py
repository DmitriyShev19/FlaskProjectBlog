import uuid

from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

manager = LoginManager(app)


@app.route('/')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route('/where_to_begin')
def where_to_begin():
    return render_template('where_to_begin.html', title='С чего начать?')


@app.route('/folk')
def folk():
    return render_template('folk.html', title='Фолклер')


if __name__ == '__main__':
    app.run(debug=True)
