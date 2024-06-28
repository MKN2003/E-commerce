from database.models import User
from database import get_db
from datetime import datetime


def get_exact_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        return user
    return "Такого пользователя не существует"


def check_user_db(username, phone_number, email):
    db = next(get_db())
    checker_name = db.query(User).filter_by(username=username).first()
    checker_phone_number = db.query(User).filter_by(phone_number=phone_number).first()
    checker_email = db.query(User).filter_by(email=email).first()
    if checker_name:
        return "Такой Username уже занят"
    elif checker_phone_number:
        return 'Такой номер телеофона уже занят'
    elif checker_email:
        return "Такой email уже занят"
    else:
        return True


def user_register_db(username, email, phone_number, address, hashed_password):
    db = next(get_db())
    checker = check_user_db(username, email, phone_number)

    if checker:
        new_user = User(username=username, email=email, phone_number=phone_number, address=address,
                        hashed_password=hashed_password, created_at=datetime.now())
        db.add(new_user)
        db.commit()
        return 'Пользователь успешно зарегистрирован'
    else:
        return checker


def user_login_db(email, hashed_password):
    db = next(get_db())
    user_email = db.query(User).filter_by(email=email).first()

    if user_email:
        if user_email.hashed_password == hashed_password:
            return user_email
        else:
            return 'Данные введены неправильно'
    else:
        return 'Такого пользователя не существует'


def user_update_info_db(id, change_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        try:
            if change_info == 'name':
                user.username = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'email':
                user_filter = db.query(User).filter_by(email=change_info).first()

                if user_filter:
                    return 'Эта почта уже занята'
                else:
                    user.email = new_info
                    db.commit()
                    return 'Успешно изменено'
            elif change_info == 'address':
                user.address = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'password':
                user.hashed_password = new_info
                db.commit()
                return 'Успешно изменено'
            elif change_info == 'number':
                user.phone_number = new_info
                db.commit()
                return 'Успешно изменено'
            else:
                return 'Таких данных не существует'
        except:
            return 'Нет такого значения для изменения'
    return False


def user_update_all_info_db(id, update_name, update_email, update_phone_number, update_address, update_password):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        user.username = update_name
        user.email = update_email
        user.phone_number = update_phone_number
        user.address = update_address
        user.hashed_password = update_password
        db.commit()
        return 'Данные успешно изменены'
    return 'Такого пользоваетеля не существует'


def delete_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()

    if user:
        db.delete(user)
        db.commit()
        return 'Пользователь успешно удален'
    return 'Такого пользователя не существует'
