from database.models import Category
from database import get_db
from datetime import datetime


def get_all_categories_db():
    db = next(get_db())
    all_categories = db.query(Category).all()
    return all_categories


def get_exact_category_db(id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=id).first()

    if category:
        return category
    return 'Такой категории не существует'


def add_category_db(category_name, product_id):
    db = next(get_db())
    if product_id:
        new_category = Category(category_name=category_name, product_id=product_id)
        db.add(new_category)
        db.commit()
        return 'Новая категория успешно добавлена'
    return 'Такого товара не существует для добавления'


def update_category_db(id, update_name):
    db = next(get_db())
    category = db.query(Category).filter_by(id=id).first()

    if category:
        category.category_name = update_name
        db.commit()
        return 'Обновлено успешно'


def delete_category_db(id):
    db = next(get_db())
    category = db.query(Category).filter_by(id=id).first()

    if category:
        db.delete(category)
        db.commit()
        return 'Категория удалена успещна'
    return 'Обновлено успешно'

