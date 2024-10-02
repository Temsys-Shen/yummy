from peewee import *
from botpy.ext.cog_yaml import read

db = SqliteDatabase("database.db")


class EatingGroup(Model):
    id = AutoField()  # 车车ID
    initiator = CharField()  # 发起人名称
    name = CharField()  # 餐厅名称
    location = CharField()  # 餐厅地点
    publish_time = DateTimeField()  # 发车时间
    end_time = DateTimeField()  # 结车时间
    remark = CharField(default="") # 备注

    class Meta:
        database = db