from fastapi import FastAPI, HTTPException

app = FastAPI()

# ロールとメソッドの対応関係
ROLE_METHOD_MAPPING = {
    "admin": ["GET", "POST", "PUT", "DELETE"],
    "user": ["GET", "HEAD"]
}

@app.get("/roles/{role}", summary="ロールに対応するHTTPメソッドを取得", response_model=dict)
async def get_role_methods(role: str):
    
    # 指定されたロールに対する許可されたHTTPメソッドのリストを返すAPI
    #role: admin, user, guest などのロール
    #methods: 対応するHTTPメソッドの配列

    methods = ROLE_METHOD_MAPPING.get(role)
    if methods:
        return {"methods": methods}
    else:
        raise HTTPException(status_code=404, detail="Role not found")
