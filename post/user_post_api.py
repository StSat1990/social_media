from fastapi import APIRouter, UploadFile, Body

from post import PublicPostValidator, EditPostValidator

from database.postservice import add_post_db, add_post_photo_db, edit_post_db, delete_post_db, get_all_posts_db, \
    get_exact_post_db

posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


# Запрос на публикации поста
@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    result = add_post_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Sorry! Not Found'}

# Запрос на изменения текста в публикации
@posts_router.put('/change_post')
async def change_post(data: EditPostValidator):
    result = edit_post_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Sorry! not found'}


# Запрос на удаления публикации
@posts_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result, 'status': 'Deleted'}
    else:
        return {'message': 'Post not found'}

# Запрос на получения всех публикаций
@posts_router.get('/get_all_posts')
async def get_all_posts():
    result = get_all_posts_db()

    return {'message': result}

# Запрос для добавления фото к посту
@posts_router.post('/add_photo')
async def add_photo(post_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None
                    ):
    photo_path = f'/media/{photo_file.filename}'
    try:
        # Сохранения фотографии в папку media
        with open(f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()

            file.write(user_photo)

        # Сохранения ссылки к фотографии в базу
        result = add_post_photo_db(post_id=post_id, post_photo=photo_path)

    except Exception as error:
        result = error

    return {'message': result}


# Получить определенный пост
@posts_router.get('/get_exact_post')
async def get_exact_post(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}