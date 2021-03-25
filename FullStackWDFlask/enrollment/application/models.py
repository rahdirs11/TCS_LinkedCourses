import flask
from application import db


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)


class Course(db.Document):
    courseID = db.StringField(max_length=10, unique=True)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=255)
    term = db.StringField(max_length=25)
    credits = db.IntField()


class Enrollment(db.Document):
    userID = db.IntField()
    courseID = db.StringField(max_length=10)
    