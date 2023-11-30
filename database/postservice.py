from .models import UserPost, PostPhoto
from datetime import datetime

from database import get_db


# Добавления поста
def add_post_db(user_id, post_text):
    db = next(get_db())

    # Создать обьект для базы данных
    new_post = UserPost(user_id=user_id,
                        post_text=post_text,
                        publish_date=datetime.now())
    db.add(new_post)
    db.commit()

    return 'Успешно добавлено'


# Добавить фото к посту
def add_post_photo_db(post_id, post_photo):
    db = next(get_db())

    new_post_photo = PostPhoto(post_id=post_id, post_photo=post_photo)

    db.add(new_post_photo)
    db.commit()

    return 'Фотография загружен'


def get_post_photo_db():
    db = next(get_db())

    new_post_photo = db.query(PostPhoto).all()

    return new_post_photo

# Изменить пост
def edit_post_db(post_id, user_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id, user_id=user_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()

        return 'Успешно изменено'
    else:
        return False


# Удалить пост
def delete_post_db(post_id):
    db = next(get_db())

    delete_post = db.query(UserPost).filter_by(id=post_id).first()
    delete_post_photo = db.query(PostPhoto).filter_by(post_id=post_id).first()

    if delete_post:
        db.delete(*delete_post_photo)
        db.commit()

        db.delete(delete_post)
        db.commit()

        return "Успешно удалено"
    else:
        return False


#     ДЗ!!!!!!!
def get_all_posts_db():
    db = next(get_db())

    all_posts = db.query(UserPost).all()
    return all_posts

def get_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(PostPhoto).filter_by(id=post_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Error'
