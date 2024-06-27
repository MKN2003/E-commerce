from fastapi import APIRouter, UploadFile, File
from database.photoservice import *

photo_router = APIRouter(tags=['Photos'], prefix='/photo')


@photo_router.post('/api/add-photo-product')
async def add_photo(product_id: int, path: UploadFile = File(...)):
    if path:
        with open(f'images/photo_{product_id}.jpg', 'wb') as photo:
            photo_to_save = await path.read()
            photo.write(photo_to_save)
            add_photo_db(product_id, f'images/photo_{product_id}.jpg')
        return 'Успешно'
    else:
        return 'Не фото не загрузилось'


@photo_router.get('/all-photos')
async def get_photos():
    all_photos = get_all_photos_db()
    return all_photos


@photo_router.delete('/api/delete-photo')
async def delete_photo(id: int):
    photo_delete = delete_photo_db(id=id)
    return photo_delete
