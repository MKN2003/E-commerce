from database.models import Order
from database import get_db


def get_all_orders_db():
    db = next(get_db())
    all_orders = db.query(Order).all()
    return all_orders


def get_order_db(id):
    db = next(get_db())
    order = db.query(Order).filter_by(id=id).first()
    if order:
        return order
    return order


def create_order_db(user_id, cart_id):
    db = next(get_db())
    if user_id and cart_id:
        new_order = Order(user_id=user_id, cart_id=cart_id)
        db.add(new_order)
        db.commit()
        return 'Заказ оформлен'
    return 'Заказ не обработан'


def delete_order_db(id):
    db = next(get_db())
    order_delete = db.query(Order).filter_by(id=id).first()

    if order_delete:
        db.delete(order_delete)
        db.commit()
    return False
