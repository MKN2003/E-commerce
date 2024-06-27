from sqlalchemy import Column, String, Integer, Float,DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    in_stock = Column(Boolean, default=True)
    created_at = Column(DateTime)


class ProductPhoto(Base):
    __tablename__ = 'product_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    photo_path = Column(String, nullable=False)
    created_at = Column(DateTime)

    post_fk = relationship(Product, foreign_keys=[product_id], lazy='subquery')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, unique=True, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))

    product_fk = relationship(Product, foreign_keys=[product_id], lazy='subquery')


class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    amount = Column(Integer, nullable=False)
    price = Column(Float)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    product_fk = relationship(Product, foreign_keys=[product_id], lazy='subquery')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    cart_id = Column(Integer, ForeignKey('carts.id'))

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    cart_fk = relationship(Cart, foreign_keys=[cart_id], lazy='subquery')


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    created_at = Column(DateTime)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    product_fk = relationship(Product, foreign_keys=[product_id], lazy='subquery')

