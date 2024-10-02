import botpy
from botpy.message import C2CMessage, GroupMessage, Message
from botpy import logging

_log = logging.get_logger()

class Client(botpy.Client):
    def _parse_message(self, message:Message):
        if message.content.startswith("/发车"):
            raise NotImplementedError("发车功能尚未实现")
        elif message.content.startswith("/查车"):
            raise NotImplementedError("查车功能尚未实现")
        elif message.content.startswith("/上车"):
            raise NotImplementedError("上车功能尚未实现")
        elif message.content.startswith("/收车"):
            raise NotImplementedError("收车功能尚未实现")
    
    async def on_ready(self):
        _log.info(f"「{self.robot.name}」 准备就绪!")

    async def on_group_at_message_create(self, message: GroupMessage):
        # messageResult = await message._api.post_group_message(
        #     group_openid=message.group_openid,
        #     msg_type=0,
        #     msg_id=message.id,
        #     content=f"收到了消息：{message.content}")
        # _log.info(messageResult)
        pass

    async def on_c2c_message_create(self, message: C2CMessage):
        
        # await message._api.post_c2c_message(
        #     openid=message.author.user_openid,
        #     msg_type=0, msg_id=message.id,
        #     content=f"我收到了你的消息：{message.content}"
        # )
        pass