import asyncio
import json

from asgiref.sync import async_to_sync, sync_to_async
from celery import shared_task
from channels.layers import get_channel_layer
from parsel import Selector
import requests

from bots import checkOrder
from bots.models import TalkTimes, UsedOrder
from loguru import logger

channel_layer = get_channel_layer()

'''

@shared_task
def add(channel_name, x, y):
    message = '{}+{}={}'.format(x, y, int(x) + int(y))
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": message})
    print(message)
'''


@shared_task
def addtimes(channel_name, orderId, id):
    logger.error(orderId)
    talkUser = TalkTimes.objects.get(userId=id)
    totleTimes = talkUser.totleTimes + 5
    residualTimes = talkUser.residualTimes + 5
    if checkOrder.checkUsedOrder(orderId):
        if len(UsedOrder.objects.filter(userId=orderId)) == 0:
            talkUser = TalkTimes.objects.get(userId=id)
            talkUser.totleTimes = totleTimes
            talkUser.residualTimes = residualTimes
            talkUser.save()

            usedOrder = UsedOrder(
                userId=orderId
            )
            usedOrder.save()
            response_message = str(orderId) + "已使用，聊天次数剩余: " + str(residualTimes)
        else:
            response_message = str(orderId) + "订单号已使用"
    else:
        response_message = str(orderId) + "订单号不存在"

    logger.debug(response_message)
    async_to_sync(channel_layer.send)(channel_name,
                                      {"type": "chat.message",
                                       "message": response_message})


'''
class PoemSpider(object):
    def __init__(self, keyword):
        self.keyword = keyword
        self.url = "https://so.gushiwen.cn/search.aspx"

    def parse_page(self):
        params = {'value': self.keyword}
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            # 创建Selector类实例
            selector = Selector(response.text)
            # 采用xpath选择器提取诗人介绍
            intro = selector.xpath('//textarea[starts-with(@id,"txtareAuthor")]/text()').get()
            print("{}介绍:{}".format(self.keyword, intro))
            if intro:
                return intro

        print("请求失败 status:{}".format(response.status_code))
        return "未找到诗人介绍。"

'''


@shared_task
def chat(channel_name, message, id):
    spider = gptHttp(message, id)
    result = spider.parse_page()
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": str(result)})
    print(result)


class gptHttp:

    def __init__(self, message_str, id):
        self.session_id = "qq-"+ str(id)
        self.url = "http://localhost:12345/v1/chat"
        self.username = "username"
        self.message = message_str
        self.result = None

    def parse_page(self):
        params = {"session_id": self.session_id,
                  "username": self.username,
                  "message": self.message}
        data_json = json.dumps(params)
        response = requests.post(self.url, data=data_json)
        print(response.json())
        flag = response.status_code=="200"
        print(flag)
        if str(response.status_code) == "200":
            logger.error(response)
            return response.json().get("message")

        print("请求失败 status:{}".format(response.status_code))
        return "未找到诗人介绍。"
