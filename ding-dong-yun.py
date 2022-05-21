"""
Python Wechaty - https://github.com/wechaty/python-wechaty
Authors:    Huan LI (李卓桓) <https://github.com/huan>
            Jingjing WU (吴京京) <https://github.com/wj-Mcat>
2020 @ Copyright Wechaty Contributors <https://github.com/wechaty>
Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import asyncio

from urllib.parse import quote

from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)


async def on_message(msg: Message):
    """
    Message Handler for the Bot
    """
    msg_src = msg.text()
    # msg_src = msg.talker.__name__
    # msg_src = msg.chatter
    # contact_1 = Contact.name()

    if msg.is_self():
        return
    if msg.text() == '是否已吃药':
        await msg.say('已吃药')

        file_box = FileBox.from_url(
            'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/'
            'u=1116676390,2305043183&fm=26&gp=0.jpg',
            name='ding-dong.jpg'
        )
        await msg.say(file_box)         
    elif msg_src.startswith('消息提醒'):
        await msg.say('请以“内容：”开头，发送你要提醒的事情')
    elif msg_src.startswith('内容'):
        await msg.say('请以“时间：”开头，发送你希望何时提醒')
    elif msg_src.startswith('时间'):
        await msg.say('将在指定时间发送提醒')
    else:
        await msg.say('这是吃药小助手: 目前的功能是\n- 收到"是否已吃药", 回复"已吃药或未吃药"\n- 收到"消息提醒", 开始消息提醒功能')
    # if msg.text() == '发送提醒':
    #     await msg.say('你要提醒什么事情')
    #     if msg.text() == '[sS]*':
    #         await msg.say('请输入发送时间')
    #         if msg.text() == '[sS]*':
    #             await msg.say('已发送提醒')


async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    """
    Scan Handler for the Bot
    """
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + quote(qrcode))


async def on_login(user: Contact):
    """
    Login Handler for the Bot
    """
    print(user)
    # TODO: To be written


async def main():
    """
    Async Main Entry
    """
    #
    # Make sure we have set WECHATY_PUPPET_SERVICE_TOKEN in the environment variables.
    # Learn more about services (and TOKEN) from https://wechaty.js.org/docs/puppet-services/
    #
    # It is highly recommanded to use token like [paimon] and [wxwork].
    # Those types of puppet_service are supported natively.
    # https://wechaty.js.org/docs/puppet-services/paimon
    # https://wechaty.js.org/docs/puppet-services/wxwork
    # 
    # Replace your token here and umcommt that line, you can just run this python file successfully!
    # os.environ['token'] = 'puppet_paimon_your_token'

    os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = 'puppet_padlocal_f8837cb790c84c31897fddcf43b36a1f'     
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan',      on_scan)
    bot.on('login',     on_login)
    bot.on('message',   on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())
