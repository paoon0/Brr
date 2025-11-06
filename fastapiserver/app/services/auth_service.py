import httpx
from app.config import settings

# 環境変数から設定を取得

async def fetch_access_token(code: str) -> str:
    
    # AuthorizationCodeを利用してアクセストークンを取得する
    
    token_url = f"https://{settings.domain}/oauth/token"
    data = {
        "grant_type": settings.grant_type,
        "client_id": settings.client_id,
        "client_secret": settings.client_secret,
        "code": code,
        "redirect_uri": settings.redirect_uri,
        "audience": settings.audience,
        "scope": settings.scope
    }

    try:
        async with httpx.AsyncClient() as client:
            token_response = await client.post(token_url, data=data)
            token_response.raise_for_status()  # ステータスコードがエラーの場合例外を発生

            token_data = token_response.json()
            access_token = token_data.get("access_token")
            print("your accesstoken:" + access_token)
            return access_token  # アクセストークンを返却

    except httpx.RequestError as e:
        print(f"HTTPリクエストエラー: {e}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"HTTPステータスエラー: {e.response.status_code}")
        return None
