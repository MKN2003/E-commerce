from database.models import Review
from database import get_db
from datetime import datetime


def get_all_reviews_db():
    db = next(get_db())
    all_reviews = db.query(Review).all()
    return all_reviews


def get_review_db(id):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()

    if review:
        return review
    return 'Такого отзыва не существует'


def add_review_db(user_id, product_id, rating, comment):
    db = next(get_db())
    if user_id and product_id:
        new_review = Review(user_id=user_id, product_id=product_id, rating=rating,
                            comment=comment, created_at=datetime.now())
        db.add(new_review)
        db.commit()
        return 'Отзыв добавлен'
    return 'Пользовтель или товар указаны неправильно'


def update_review_db(id, update_rating, update_comment):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()

    if review:
        review.rating = update_rating
        review.comment = update_comment
        db.commit()
        return 'Отзыв изменен'
    return 'Такого отзыва не существует'


def delete_review_db(id):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()

    if review:
        db.delete(review)
        db.commit()
        return 'Отзыв успешно удален'
    return 'Такого отзыва не существует'
