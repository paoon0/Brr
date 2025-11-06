from fastapi import APIRouter, HTTPException
from app.db.models import Task
from app.services.task_service import get_tasks_service, create_task_service,delete_task_service
from fastapi import Response
import os

router = APIRouter()

# タスク取得用エンドポイント そもそもtokenが有効でないとエンドポイントにアクセス不可
@router.get("/getmytask")
async def get_tasks():
    try:
        tasks = await get_tasks_service()
        print(tasks)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail="タスク取得エラー")


# タスク作成用エンドポイント
@router.post("/createtask")
async def create_task(task: Task):
    try:
        task_id = await create_task_service(task)
        return {"id": task_id, "title": task.title}
    except Exception as e:
        raise HTTPException(status_code=500, detail="タスク作成エラー")


# タスク削除エンドポイント
@router.delete("/deletetask/{task_id}")
async def delete_task(task_id: int):
    try:
        message = await delete_task_service(task_id)
        return {"message": message}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="タスク削除エラー")
    
# テスト用エンドポイント
@router.get("/needauth")
async def needauthu():
        return {"message": "Hello World!!"}

# ユーザのタスク一覧の枠組みをhtmlで返す
# authpointからリクエストが送信される
@router.get("/userindex")
async def authpoint():
        # mytask.html を開いてその内容を読み込む
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir,"..", "templates", "mytask2.html")
        with open(file_path, "r",encoding="utf-8") as file:
            content = file.read()

        # 読み込んだ内容を text/html メディアタイプで返す
        return Response(content=content, media_type="text/html")
