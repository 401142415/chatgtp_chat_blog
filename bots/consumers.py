import asyncio
import json
import time

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from loguru import logger

from . import tasks, checkOrder

COMMANDS = {
    'help': {
        'help': '命令帮助信息.',
    },
    'check': {
        'help': '显示剩余次数.',
    },
    'addtimes': {
        'args': 1,
        'help': '添加次数，例子: `addtimes 订单号`.',
        'task': 'addtimes'
    },
    'chat': {
        'args': 2,
        'help': '输入文本直接聊天',
        'task': 'chat'
    }


}

class BotConsumer(WebsocketConsumer):
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        id = text_data_json['id']
        name =  text_data_json['name']
        print(str(id)+ "|"+str(name)+ " say:" + message)
        response_message = '请输入`help`获取命令帮助信息。'
        message_parts = message.split()
        if message_parts:
            command = message_parts[0].lower()
            # todo 这里加入余额充值，先查询订单号是否本地有，若无，在查询是否在远程有已使用，增加次数、插入订单信息
            if command == 'help':
                response_message = '支持的命令有:\n' + '\n'.join(
                    [f'{command} - {params.get("help", "")} ' for command, params in COMMANDS.items()])
                self.send_message(response_message)
            elif command == 'check':
                response_message = f'剩余次数为' + str(checkOrder.checkTimes(id))
                self.send_message(response_message)

            elif command == 'addtimes':
                response_message = f'!! {message}'
                self.send_message(response_message)
                getattr(tasks, COMMANDS["addtimes"]['task']).delay(self.channel_name, message_parts[1] , id)
                '''
            elif command in COMMANDS:
                if len(message_parts[1:]) != COMMANDS[command]['args']:
                    response_message = f'命令`{command}`参数错误，请重新输入.'
                else:
                    # BotConsumer 在接收到路由转发的前端消息后，对其解析，
                    # 将当前频道名和解析后的参数一起交由 Celery 异步执行。
                    # Celery 执行任务完成以后会将结果发到这个频道，这样就实现了 channels 和 Celery 的通信。
                    getattr(tasks, COMMANDS[command]['task']).delay(self.channel_name, *message_parts[1:])
                    response_message = f'!!{message}'
                '''
            else:
                if int(checkOrder.checkTimes(id))>0:
                    response_message = f'!!{message}'
                    self.send_message(response_message)
                    getattr(tasks, COMMANDS["chat"]['task']).delay(self.channel_name, message, id)

                    checkOrder.reductionTimes(id)

                    # tasks.chat(self.channel_name, message , id)
                else:
                    response_message = '剩余聊天次数不足，请使用"addtimes 订单号"命令增加次数'
                    self.send_message(response_message)


    def send_message(self,response_message):
        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                'type': 'chat.message',
                'message': response_message
            }
        )
    def chat_message(self, event):
        message = event['message']
        if not str(message).startswith("!!"):
            # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': f'[机器人] {message}'
            }))
        else:
            # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': f'[你] {message[2:]}'
            }))