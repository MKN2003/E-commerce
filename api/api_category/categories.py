from fastapi import APIRouter
from database.categoryservice import *

category_router = APIRouter(tags=['Categories'], prefix='/categories')


@category_router.get('all-categories')
async def get_all_categories():
    all_categories = get_all_categories_db()
    return all_categories


@category_router.get('api/category')
async def get_category(id: int):
    category = get_exact_category_db(id=id)
    return category


@category_router.post('api/add-category')
async def add_category(category_name: str, product_id: int):
    new_category = add_category_db(category_name=category_name, product_id=product_id)
    return new_category


@category_router.put('api/update-category')
async def update_category(id: int, update_name: str):
    category_update = update_category_db(id=id, update_name=update_name)
    return category_update


@category_router.delete('api/delete-category')
async def delete_category(id: int):
    category_delete = delete_category_db(id=id)
    return category_delete