from botpy.message import GroupMessage
from .models import EatingGroup
import datetime
import re

发车模板 = """
下面是发车模板：
【发起人】胡图图
【餐厅名称】胡图图家常菜
【餐厅地点】翻斗大街 翻斗花园 二号楼1001室
【结车时间】7（小时为单位，不填默认72小时）
【备注】今晚7点，来之前打电话+11 45141919810（不填默认为空）
建议复制下半部分文字，然后填写完整后发送
【发起人】
【餐厅名称】
【餐厅地点】
【结车时间】
【备注】
"""


async def start(message: GroupMessage):
    try:
        if ("【餐厅名称】" not in message.content) or ("【餐厅地点】" not in message.content) or ("【发起人】" not in message.content):
            raise ValueError("没有填写餐厅名称或餐厅地点或发起人")

        messages = ("【发起人】" + message.content.split("【发起人】")
                    [1:][-1]).split("\n")
        useful_messages = {}
        for msg in messages:
            if msg[:1] == "【":
                key = msg.split("】")[0].replace("【", "")
                value = msg.split("】")[1]
                useful_messages[key] = value
                
        # 如果没有填写餐厅名称或餐厅地点，提示用户
        if useful_messages["餐厅名称"] == "" or useful_messages["餐厅地点"] == "" or useful_messages["发起人"] == "":
            raise ValueError("没有填写餐厅名称或餐厅地点或发起人")
        # 提取结车时间中的数字部分
        if "结车时间" in useful_messages:
            match = re.search(r'\d+', useful_messages["结车时间"])
            if match:
                useful_messages["结车时间"] = match.group()
            else:
                useful_messages["结车时间"] = "72"
        else:
            useful_messages["结车时间"] = "72"
        if int(useful_messages["结车时间"]) <= 0:
            raise ValueError("结车时间有点问题哦")
        # 如果没有填写备注，默认为空
        if "备注" not in useful_messages:
            useful_messages["备注"] = ""
        # 结车时间变成当前时间+结车时间的datetime格式
        useful_messages["结车时间"] = datetime.datetime.now() + datetime.timedelta(hours=int(useful_messages["结车时间"]))
        feedback = f'【发起人】：{useful_messages["发起人"]}\n【餐厅名称】：{useful_messages['餐厅名称']}\n【餐厅地点】：{useful_messages['餐厅地点']}\n【结车时间】：{useful_messages['结车时间']}\n【备注】：{useful_messages['备注']}'
        group = EatingGroup(initiator=useful_messages["发起人"],
                                   name=useful_messages["餐厅名称"], 
                                   location=useful_messages["餐厅地点"], 
                                   publish_time=datetime.datetime.now(),
                                   end_time=useful_messages["结车时间"], 
                                   remark=useful_messages["备注"])
        group.save()
        await message.reply(content=f"发车成功！请确认信息：\n{feedback}")
    except ValueError as e:
        await message.reply(content=f"格式不对哦，{str(e)}\n{发车模板}")

# 查车
async def search(message: GroupMessage):
    print(message.content)
    #/查车或者/查车 ID，都要适配
    messages = message.content.strip().split("/查车",1)
    print(messages)
    if messages[1].strip() == "":
        #/查车
        groups = EatingGroup.select()
        if len(groups) == 0:
            await message.reply(content="没有车车哦")
        else:
            for group in groups:
                await message.reply(content=f"【发起人】：{group.initiator}\n【餐厅名称】：{group.name}\n【餐厅地点】：{group.location}\n【结车时间】：{group.end_time}\n【备注】：{group.remark}")
    else:
        #/查车 ID
        try:
            group_id = int(messages[1])
            group = EatingGroup.get(EatingGroup.id == group_id)
            await message.reply(content=f"【发起人】：{group.initiator}\n【餐厅名称】：{group.name}\n【餐厅地点】：{group.location}\n【结车时间】：{group.end_time}\n【备注】：{group.remark}")
        except EatingGroup.DoesNotExist:
            await message.reply(content="没有这个车车哦")
        except ValueError:
            await message.reply(content="ID必须是数字哦")
    


async def stop(message: GroupMessage):
    pass
