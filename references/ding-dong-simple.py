import asyncio
import os
from wechaty import FileBox, Wechaty, Message

class MyBot(Wechaty):
    async def on_message(self, msg: Message):
        talker = msg.talker()
        await talker.ready()
        if msg.text() == "ding":
            await talker.say('dong')
        elif msg.text() == 'image':
            file_box = FileBox.from_url(
                'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/'
                'u=1116676390,2305043183&fm=26&gp=0.jpg',
                name='ding-dong.jpg')
            await talker.say(file_box)

async def main():
    os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = 'puppet_padlocal_65b98b3be0b9493dabe65cb3be7bcff7'
    bot = MyBot()
    await bot.start()

asyncio.run(main())