from fastapi import APIRouter
from database.cartservice import *
from database.models import Cart, Product

cart_router = APIRouter(tags=['Carts'], prefix='/carts')


@cart_router.get('/all-carts')
async def get_all_carts():
    all_carts = get_all_carts_db()
    return all_carts


@cart_router.get('/api/get-cart')
async def get_cart(id: int):
    cart = get_cart_db(id=id)
    return cart


@cart_router.post('/api/add-product-to-cart')
async def add_product_to_cart(user_id: int, product_id: int, amount: int, price: float):
    add_item = add_product_to_cart_db(user_id=user_id, product_id=product_id, amount=amount, price=price)
    return add_item


@cart_router.delete('/api/delete-cart-item')
async def delete_cart(id: int):
    cart_delete = delete_cart_db(id=id)
    return cart_delete

