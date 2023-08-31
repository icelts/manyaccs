from tortoise.models import Model
from tortoise import fields

class orders(Model):  #存储订单信息的表
    id = fields.IntField(pk=True)
    ordercontent = fields.TextField()
    productid = fields.TextField()
    userids = fields.TextField(description="购买用户ID")
    charged = fields.FloatField(description="订单扣款")
    ordertime = fields.DatetimeField(description="售出时间")

class products(Model):  #存储商品简介信息
    id = fields.IntField(pk=True)
    name = fields.TextField(description="商品名字")
    jianjie = fields.TextField(description="商品描述")
class kami(Model): #存放的卡密信息
    id = fields.IntField(pk=True)
    type = fields.IntField(description="product id")
    kamicontent = fields.TextField(description="卡密内容")
    status = fields.IntField(default=1, description="卡密状态，1为未出售")
    creatted = fields.DatetimeField(description="卡密创建时间")
    soldtime = fields.DatetimeField(description="售出时间")
class users(Model): #用户信息
    id = fields.IntField(pk=True)
    token = fields.CharField(max_length=32,description="用户的token")
    balance = fields.IntField (default=0, description="余额")
    status = fields.IntField(default=1, description="用户状态，1为激活状态")
    lastactive = fields.DatetimeField()
    creattime = fields.DatetimeField()