from .models import User

from database import get_db

from datetime import datetime


# Регистрация пользователя
def register_user_db(name, surname, email,
                     phone_number, city, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return 'Такой пользователь уже есть'

    new_user = User(name=name, surname=surname, email=email,
                    phone_number=phone_number, city=city, password=password,
                    reg_date=datetime.now())
    db.add(new_user)
    db.commit()

    return 'Успешно прошли регистрацию'


# Логин пользователя
def login_user_db(email, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    else:
        return 'Ошибка в данных'


# Добавить фото профиля
def add_profile_photo_db(profile_photo, user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(id=user_id).first()

    if checker:
        checker.profile_photo = profile_photo
        db.commit()

        return 'Фото профиля добавлен'
    else:
        return False


# Удаления фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(id=user_id).first()

    if checker:
        checker.profile_photo = 'None'
        db.commit()

        return 'Фото провфиля удалено'
    else:
        return False

# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

# Получить информацию про определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    return exact_user

# Изменить данные пользователя и фотография(ДЗ)
# def edit_user_db
# def edit_profile_photo_db
