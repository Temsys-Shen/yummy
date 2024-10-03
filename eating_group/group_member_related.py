from botpy.message import GroupMessage
from .models import EatingGroupMember, EatingGroup

# 上车
async def join(message: GroupMessage):
    """
    上车
    /上车 车车ID 称呼
    """
    try:
        contents = message.content.split("/上车")[1].strip().split(" ", 1)
        group_id = contents[0]
        name = contents[1]
        group:EatingGroup = EatingGroup.get(EatingGroup.id == group_id)
        
        if "'" in name or '"' in name:
            await message.reply(content="不要输入奇怪的东西哦")
            return
        
        # 重复上车
        if EatingGroupMember.select().where(
            (EatingGroupMember.group_id == group_id) & 
            (EatingGroupMember.menber_id == message.author.member_openid)
        ).exists():
            await message.reply(content="你已经在这个车车里了")
            return
        
        EatingGroupMember.create(group_id=group_id, name=name, menber_id=message.author.member_openid)
        await message.reply(content=f"上车成功, 「{name}」上了「{group.name}」的车车")
    except IndexError:
        await message.reply(content="请按照「/上车 车车ID 称呼」格式有序上车")
    except EatingGroup.DoesNotExist:
        await message.reply(content="没有这个车车哦")
        
# 下车
async def leave(message: GroupMessage):
    """
    下车
    /下车 车车ID
    """
    try:
        group_id = message.content.split("/下车")[1].strip()
        group:EatingGroup = EatingGroup.get(EatingGroup.id == group_id)
        member:EatingGroupMember = EatingGroupMember.get(
            (EatingGroupMember.group_id == group_id) & 
            (EatingGroupMember.menber_id == message.author.member_openid)
        )
        member.delete_instance()
        await message.reply(content=f"下车成功, 「{member.name}」下了「{group.name}」的车车")
    except EatingGroup.DoesNotExist:
        await message.reply(content="没有这个车车哦")
    except EatingGroupMember.DoesNotExist:
        await message.reply(content="你不在这个车车里哦")
    except IndexError:
        await message.reply(content="格式不对哦，/下车 车车ID")
    except ValueError:
        await message.reply(content="格式不对哦，/下车 车车ID")
    except Exception as e:
        await message.reply(content=f"未知错误：{e}")