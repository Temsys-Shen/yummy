import botpy
from botpy.message import GroupMessage
from botpy import logging
from eating_group import group_related

_log = logging.get_logger()


class Client(botpy.Client):
    async def _parse_message(self, message: GroupMessage):
        if "/发车" in message.content:
            await group_related.start(message)
        elif "/查车" in message.content:
            await group_related.search(message)
        elif "/上车" in message.content:
            raise NotImplementedError("上车功能尚未实现")
        elif "下车" in message.content:
            raise NotImplementedError("下车功能尚未实现")
        elif "/收车" in message.content:
            raise NotImplementedError("收车功能尚未实现")
        else:
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"{message.content}是错误的消息格式，请输入正确的指令")
            _log.info(messageResult)

    async def on_ready(self):
        _log.info(f"「{self.robot.name}」 准备就绪!")

    async def on_group_at_message_create(self, message: GroupMessage):
        await self._parse_message(message)
