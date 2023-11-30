from fastapi import APIRouter, UploadFile

photo_router = APIRouter(prefix='/photo', tags=['Фотографии'])


# Добавления фото(для аватарки)
@photo_router.post('/add-photo')
async def add_user_profile_photo(photo_file: UploadFile, user_id: int):
    # Сохранить локально фото
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    return {'message': 'Successfully'}


# Изменения фото(для аватарки)
@photo_router.put('/edit-photo')
async def edit_user_profile_photo(new_photo_file: UploadFile, user_id: int):
    # Сохранить локально фото
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()

        file.write(user_photo)

    return {'message': 'Successfully'}


# Удаления фото(для аватарки)
@photo_router.delete('/delete-photo')
async def delete_user_profile_photo(user_id: int):
    pass
