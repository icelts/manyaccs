#检测APIkey的合法性以及返回结果
from dbmodel import users
async def checktoken(apikey):
        user = await users.get(token = apikey)
        print(user.token)
