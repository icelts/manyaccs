from fastapi import FastAPI
from dbmodel import *
app = FastAPI()
'''
#接口功能列表
token检测，余额查询，扣费
'''''
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/stubs/handler_api.php?api_key={api_key}",tags=["api v2"], summary="get balance")
async def actions(api_key, action:str):
    if action == "getbalance":
        print("test hello")
        user = await users.get(token=api_key)
        if user:
            return {"status": "200", "ret": user.balance}
        else:
            return {"status": "400", "ret": "balance check error"}


