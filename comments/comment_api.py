from fastapi import APIRouter

from comments import CommentValidator, EditCommentValidator

from database.commentservice import add_comment_db, edit_comment_db, delete_comment_db, get_post_comments

comment_router = APIRouter(prefix='/comment', tags=['Работа с коментариями'])

# Запрос на публикацию коментария
@comment_router.post('/add_comment')
async def add_comment(data: CommentValidator):
    pass

# Запрос на изменения коментарий
@comment_router.put('/edit_comment')
async def edit_comment(data: EditCommentValidator):
    pass

# Запрос на удаления комента
@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    pass

# Запрос на получения коментариев к определенному посту
@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    pass
