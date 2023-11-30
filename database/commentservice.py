from .models import Comment

from datetime import datetime

from database import get_db


# Добавить коментарий
def add_comment_db(user_id, comment_text, post_id):
    db = next(get_db())

    new_comment = Comment(post_id=post_id, comment_text=comment_text, user_id=user_id)

    db.add(new_comment)
    db.commit()

    return "Коментарий успешно добавлен"


# Изменения определенный коментарий
def edit_comment_db(comment_id, new_comment):
    db = next(get_db())

    edit_comment = db.query(Comment).filter_by(id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = new_comment
        db.commit()

        return 'Коментарий успешно изменен'
    else:
        return False


# Удаление коментарий
def delete_comment_db(comment_id):
    db = next(get_db())

    delete_comment = db.query(Comment).filter_by(id=comment_id).first()

    if delete_comment:
        db.delete(delete_comment)
        db.commit()

        return "Успешно удален"
    else:
        return False


# Получить все коментарий определенного поста
def get_post_comments(post_id):
    db = next(get_db())

    post_comment = db.query(Comment).filter_by(post_id=post_id).first()
    return post_comment
