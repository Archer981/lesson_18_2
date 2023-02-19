from flask import request
from flask_restx import Resource, Namespace
from models import Review, ReviewSchema
from setup_db import db

review_ns = Namespace('reviews')


@review_ns.route('/')
class ReviewsView(Resource):
    def get(self):
        reviews = Review.query.all()
        return ReviewSchema(many=True).dump(reviews), 200

    def post(self):
        new_data = request.json
        new_review = Review(**new_data)
        db.session.add(new_review)
        db.session.commit()
        return '', 201


@review_ns.route('/<int:rid>')
class ReviewView(Resource):
    def get(self, rid):
        review = Review.query.get(rid)
        return ReviewSchema().dump(review), 200

    def put(self, rid):
        review = Review.query.get(rid)
        new_data = request.json
        review.user = new_data.get('user', review.user)
        review.rating = new_data.get('rating', review.rating)
        review.book_id = new_data.get('book_id', review.book_id)
        db.session.add(review)
        db.session.commit()
        return '', 201

    def delete(self, rid):
        review = Review.query.get(rid)
        db.session.delete(review)
        db.session.commit()
        return '', 201
