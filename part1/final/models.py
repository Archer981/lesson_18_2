# текст задания находится в файле app.py
from marshmallow import fields, Schema
from setup_db import db


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)
    pages = db.Column(db.Integer)


class BookSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    author = fields.String()
    year = fields.Integer()
    pages = fields.Integer()


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    book_id = db.Column(db.Integer)


class ReviewSchema(Schema):
    id = fields.Integer()
    user = fields.String()
    rating = fields.Integer()
    book_id = fields.Integer()
