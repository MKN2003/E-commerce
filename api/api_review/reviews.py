from fastapi import APIRouter
from database.reviewservice import *

review_router = APIRouter(tags=['Reviews'], prefix='/reviews')


@review_router.get('/all-reviews')
async def get_all_reviews():
    all_reviews = get_all_reviews_db()
    return all_reviews


@review_router.get('/api/get-review')
async def get_review(id: int):
    review = get_review_db(id=id)
    return review


@review_router.post('/api/add-review')
async def add_review(user_id: int, product_id: int, rating: int, comment: str):
    new_review = add_review_db(user_id=user_id, product_id=product_id, rating=rating, comment=comment)
    return new_review


@review_router.put('/api/update-review')
async def update_review(id: int, update_rating: int, update_comment: str):
    review_update = update_review_db(id=id, update_rating=update_rating, update_comment=update_comment)
    return review_update


@review_router.delete('/api/delete-review')
async def delete_review(id: int):
    review_delete = delete_review_db(id=id)
    return review_delete


