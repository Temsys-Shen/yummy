import botpy
import mysparkai
from botpy.message import GroupMessage
from botpy import logging
from eating_group import group_related, group_member_related

_log = logging.get_logger()


class Client(botpy.Client):
    async def _parse_message(self, message: GroupMessage):
        if "/发车" in message.content:
            await group_related.start(message)
        elif "/查车" in message.content:
            await group_related.search(message)
        elif "/上车" in message.content:
            await group_member_related.join(message)
        elif "下车" in message.content:
            await group_member_related.leave(message)
        elif "/收车" in message.content:
            await group_related.stop(message)
        else:
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"{await mysparkai.generate_response(message.content)}")
            _log.info(messageResult)

    async def on_ready(self):
        _log.info(f"「{self.robot.name}」 准备就绪!")

    async def on_group_at_message_create(self, message: GroupMessage):
        await self._parse_message(message)
