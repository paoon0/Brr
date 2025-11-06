import pymysql
from app.config import settings

def get_db_connection():
    return pymysql.connect(
        host=settings.mysql_host,
        user=settings.mysql_user,
        password=settings.mysql_password,
        database=settings.mysql_db
    )
