"""doc"""
import asyncio
import logging
import os
from typing import Optional, Union

from wechaty_puppet import FileBox, ScanStatus  # type: ignore

from wechaty import Wechaty, Contact
from wechaty.user import Message, Room

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class ElderlyAssistant(Wechaty):
    def __init__(self):
        super().__init__()

    async def on_message(self, msg: Message):
        """
        listen for message event
        """
        from_contact = msg.talker()
        text = msg.text()
        room = msg.room()
        if msg.chatter().contact_id == 'weixin':
            return
        if text == '#ding':
            conversation: Union[
                Room, Contact] = from_contact if room is None else room
            await conversation.ready()
            await conversation.say('dong')
            file_box = FileBox.from_url(
                'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/'
                'u=1116676390,2305043183&fm=26&gp=0.jpg',
                name='ding-dong.jpg')
            await conversation.say(file_box)
        elif text == '1':
            await msg.say('天气预报')
        else:
            # await msg.say('这是吃药小助手: 目前的功能是\n- 收到"是否已吃药", 回复"已吃药或未吃药"\n- 收到"消息提醒", 开始消息提醒功能')
            await msg.say('小助手菜单：\n- 1.拨打微信视频电话\n- 2.拨打手机电话\n- 3.热点新闻\n- 4.疫情最新消息')
            await msg.say('回复对应阿拉伯数字查看详情')

    async def on_login(self, contact: Contact):
        print(f'user: {contact} has login')

    async def on_scan(self, status: ScanStatus, qr_code: Optional[str] = None,
                      data: Optional[str] = None):
        contact = self.Contact.load(self.contact_id)
        print(f'user <{contact}> scan status: {status.name} , '
              f'qr_code: {qr_code}')


bot: Optional[ElderlyAssistant] = None


async def main():
    os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = 'puppet_padlocal_65b98b3be0b9493dabe65cb3be7bcff7'
    global bot
    bot = ElderlyAssistant()
    await bot.start()


asyncio.run(main())
