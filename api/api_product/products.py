from fastapi import APIRouter
from database.productservice import *

product_router = APIRouter(tags=['Products'], prefix='/products')


@product_router.get('/all-products')
async def get_all_products():
    all_products = get_all_products_db()
    return all_products


@product_router.get('/api/get-product')
async def get_exact_product(id):
    product = get_product_db(id=id)
    return product


@product_router.post('/api/add-product')
async def add_product(product_name: str, description: str, price: float, amount: int, in_stock: bool):
    product_add = add_product_db(product_name=product_name, description=description, price=price,
                                 amount=amount, in_stock=in_stock)
    return product_add


@product_router.put('api/update-all-info')
async def update_all_info(id: int, update_name: str, update_des: str,  update_price: float, update_amount: int, in_stock: bool):
    new_data = product_update_all_info_db(id=id, update_name=update_name, update_des=update_des,
                                          update_amount=update_amount, update_price=update_price, in_stock=in_stock)
    return new_data


@product_router.patch('api/upadte-info')
async def update_info(id: int, change_info: str, new_info):
    new_data = update_product_db(id=id, change_info=change_info, new_info=new_info)
    return new_data


@product_router.delete('api/delete')
async def delete_product(id: int):
    product = delete_product_db(id=id)
    return product
