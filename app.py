import uuid

from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

manager = LoginManager(app)
