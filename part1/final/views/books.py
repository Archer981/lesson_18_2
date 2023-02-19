from flask import request
from flask_restx import Resource, Namespace
from models import Book, BookSchema
from setup_db import db

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        books = Book.query.all()
        return BookSchema(many=True).dump(books), 200

    def post(self):
        new_data = request.json
        new_book = Book(**new_data)
        db.session.add(new_book)
        db.session.commit()
        return '', 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        book = Book.query.get(bid)
        return BookSchema().dump(book), 200

    def put(self, bid):
        book = Book.query.get(bid)
        new_data = request.json
        book.name = new_data.get('name', book.name)
        book.author = new_data.get('author', book.author)
        book.year = new_data.get('year', book.year)
        book.pages = new_data.get('pages', book.pages)
        db.session.add(book)
        db.session.commit()
        return '', 201

    def delete(self, bid):
        book = Book.query.get(bid)
        db.session.delete(book)
        db.session.commit()
        return '', 201
