from fastapi import FastAPI
from app.routers import tasks, auth

app = FastAPI()

# ルーターの登録
app.include_router(tasks.router)
app.include_router(auth.router)
