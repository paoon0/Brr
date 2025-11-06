from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MySQL 接続情報
    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str

    # Auth0 設定
    grant_type: str
    client_id: str
    client_secret: str
    domain: str
    redirect_uri: str
    audience: str
    scope: str

    class Config:
        env_file = ".env"

# 設定をインスタンス化
settings = Settings()
