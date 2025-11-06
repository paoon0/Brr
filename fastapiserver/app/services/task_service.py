from app.db.connection import get_db_connection
import pymysql
from pymysql import MySQLError
from fastapi import HTTPException
from app.db.models import Task

# 環境変数から設定を取得

async def get_tasks_service() :
    """
    タスク作成のクエリを作成
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        connection.close()
        return {"tasks": tasks}
    except MySQLError as e:  # エラークラスがMySQLErrorに変更
        print("タスク取得エラー:", e)
        raise HTTPException(status_code=500, detail="タスク作成エラー")

async def create_task_service(task : Task) :
    try:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        query = "INSERT INTO tasks (title) VALUES (%s)"
        cursor.execute(query, (task.title,))
        connection.commit()
        return cursor.lastrowid
    except MySQLError as e:
        print(f"MySQLError:{e}")
        raise
    finally:
        cursor.close()
        connection.close()
        
async def delete_task_service(task_id: int) :
    try:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        query = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(query, (task_id,))
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="タスクが見つかりません")
        return "タスク削除成功"
    except MySQLError as e:
        print("タスク削除エラー:", e)
        raise HTTPException(status_code=500, detail="タスク削除エラー")
    finally:
        if cursor:
            cursor.close()
        connection.close()