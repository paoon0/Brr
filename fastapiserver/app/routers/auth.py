from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.services.auth_service import fetch_access_token

router = APIRouter()

@router.get("/authpoint")
async def get_token(request: Request):
    code = request.query_params.get("code")
    if not code:
        return {"error": "Authorization code not found"}
    
    access_token = await fetch_access_token(code)
    if not access_token:
        return {"error": "Failed to fetch access token"}
    # envoy接続
    redirect_response = RedirectResponse(url="/userindex", status_code=302)
    redirect_response.set_cookie(
        key="Authorization",
        value=access_token,
        httponly=True,
        secure=False, # HTTPS環境ならTrue
        samesite="Lax"
        )# Cookie送信の範囲を制限
    return redirect_response
