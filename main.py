from fastapi import FastAPI

from comments.comment_api import comment_router
from photo.photo_api import photo_router
from post.user_post_api import posts_router
from user.user_api import user_router
# Для запуска БД
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")


app.include_router(photo_router)
app.include_router(user_router)
app.include_router(posts_router)
app.include_router(comment_router)

@app.get('/test')
async def test():
    return 'This is test page'
