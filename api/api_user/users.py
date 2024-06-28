from fastapi import APIRouter
from database.userservice import *
from typing import Optional
from pydantic import BaseModel

user_router = APIRouter(tags=['Users'], prefix='/users')


class UserValidator(BaseModel):
    username: str
    phone_number: str
    email: str
    address: str
    hashed_password: str


@user_router.get('/all-users')
async def get_all_users():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


@user_router.get('/api/get-user')
async def get_exact_user(id: int):
    user = get_exact_user_db(id=id)
    return user


@user_router.post('/api/registration')
async def register_user(validator: UserValidator):
    db = next(get_db())
    user_data = validator.dict()
    user_email = user_data.get('email')
    print(user_email)
    checker = db.query(User).filter_by(email=user_email).first()
    print(f'ошибка {checker}')
    if not checker:
        try:
            reg_user = user_register_db(**user_data)
            return {'status': 1, "message": reg_user}
        except Exception as e:
            return {'status': 0, 'message': str(e)}
    else:
        return {'status': 0, 'message': 'Invalid email'}


@user_router.post('/api/login')
async def user_login(email, hashed_password):
    login_user = user_login_db(email=email, hashed_password=hashed_password)
    return login_user


@user_router.put('/api/update-all-info')
async def user_update_all_info(id: int, update_name, update_email, update_phone_number, update_address, update_password):
    data = user_update_all_info_db(id=id, update_name=update_name, update_email=update_email, update_phone_number=update_phone_number,
                                   update_address=update_address, update_password=update_password)
    return data


@user_router.patch('/api/update-info')
async def update_info(id: int, change_info: str, new_info: str):
    data = user_update_info_db(id=id, change_info=change_info, new_info=new_info)
    return data


@user_router.delete('/api/delete-user')
async def delete_user(id: int):
    user = delete_user_db(id=id)
    return user
