from peewee import *
from botpy.ext.cog_yaml import read

db = SqliteDatabase("database.db")


class EatingGroup(Model):
    id = AutoField()  # 车车ID
    owner_id = CharField()
    initiator = CharField()  # 发起人名称
    name = CharField()  # 餐厅名称
    location = CharField()  # 餐厅地点
    publish_time = DateTimeField()  # 发车时间
    end_time = DateTimeField()  # 结车时间
    remark = CharField(default="") # 备注

    class Meta:
        database = db
        
# 上车记录
class EatingGroupMember(Model):
    id = AutoField()
    group_id = ForeignKeyField(EatingGroup, backref="members") # 车车ID
    name = CharField() # 上车人名称
    menber_id = CharField() # 上车人ID

    class Meta:
        database = db