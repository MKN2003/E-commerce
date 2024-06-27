from database.models import ProductPhoto
from database import get_db
from datetime import datetime


def add_photo_db(product_id, photo_path):
    db = next(get_db())
    photo = ProductPhoto(product_id=product_id, photo_path=photo_path, created_at=datetime.now())
    db.add(photo)
    db.commit()
    return f'Успешно добавлен'


def get_all_photos_db():
    db = next(get_db())
    all_photos = db.query(ProductPhoto).all()
    return all_photos


def delete_photo_db(id):
    db = next(get_db())
    photo = db.query(ProductPhoto).filter_by(id=id).first()

    if photo:
        db.delete(photo)
        db.commit()
        return 'Фотография успешно удалена'
    return 'Такой фотографии не существует'

