import datetime
from flask_login import UserMixin
from app import db, manager, app


class BaseModel:
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(cls, *args, **kwargs):
        new_user = cls(*args, **kwargs)
        new_user.save()


class Users(db.Model, BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class Post(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(255), nulllable=False)
    content = db.Column(db.Text(), nulllable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


with app.app_context():
    db.create_all()