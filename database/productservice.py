from database.models import Product
from database import get_db
from datetime import datetime


def add_product_db(product_name, description, price, amount, in_stock):
    db = next(get_db())
    new_product = Product(product_name=product_name, description=description, price=price,
                          amount=amount, in_stock=in_stock, created_at=datetime.now())
    db.add(new_product)
    db.commit()
    return 'Товар успешно добавлен'


def product_update_all_info_db(id, update_name, update_des, update_price, update_amount, in_stock):
    db = next(get_db())
    product = db.query(Product).filter_by(id=id).first()

    if product:
        product.product_name = update_name
        product.description = update_des
        product.price = update_price
        product.amount = update_amount
        product.in_stock = in_stock
        db.commit()
        return 'Данные успешно изменены'
    return 'Такого пользоваетеля не существует'


def update_product_db(id, change_info, new_info):
    db = next(get_db())
    product = db.query(Product).filter_by(id=id).first()

    if product:
        try:
            if change_info == 'name':
                product.name = new_info
                db.commit()
                return 'Название продукта изменено'
            elif change_info == 'description':
                product.description = new_info
                db.commit()
                return 'Описание успешно изменено'
            elif change_info == 'price':
                product.price = new_info
                db.commit()
                return 'Цена товара изменена'
            elif change_info == 'amount':
                product.amount = new_info
                db.commit()
                return 'Количество товара изменено'
            else:
                return 'Таких данных не существует'
        except:
            return 'Таких значиений не существует для изменения'
    return False


def delete_product_db(id):
    db = next(get_db())
    product_delete = db.query(Product).filter_by(id=id).first()
    db.delete(product_delete)
    db.commit()
    return 'Товар успешно удален'


def get_product_db(id):
    db = next(get_db())
    product = db.query(Product).filter_by(id=id).first()

    if product:
        return product
    return 'Такого товара не существует'


def get_all_products_db():
    db = next(get_db())
    all_products = db.query(Product).all()
    return all_products



