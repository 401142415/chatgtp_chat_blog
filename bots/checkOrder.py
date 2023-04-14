import json

import requests
from asgiref.sync import sync_to_async
from loguru import logger

from channels.db import database_sync_to_async
from bots.models import TalkTimes

url9001 = "http://192.168.0.2:8001/GetReportList"
url10001 = "http://192.168.0.2:9001/GetReportList"
url11001 = "http://192.168.0.2:10001/GetReportList"
def checkUsedOrder(orderId):
    try:
        data = {'tid1': str(orderId), 'select': '4'}
        ret9001 = requests.post(url=url9001,  data=json.dumps(data))
        ret10001 = requests.post(url=url10001,  data=json.dumps(data),)
        ret11001 = requests.post(url=url11001,  data=json.dumps(data),)

        response_data9001 = ret9001.json()
        response_data10001 = ret10001.json()
        response_data11001 = ret11001.json()
        if len(response_data9001['d'])+len(response_data10001['d'])+len(response_data11001['d'])>0:
            return True
    except Exception as e:
        logger.info('getCapacityData [Error]: ' + str(e))
        return False
    return False

# 检测剩余次数
def checkTimes(userId):
    talkUser = TalkTimes.objects.get(userId=userId)
    return talkUser.residualTimes
# 检测剩余次数
@database_sync_to_async
def checkTimes2(userId):
    talkUser = TalkTimes.objects.get(userId=userId)
    return talkUser.residualTimes
# 减少次数


def reductionTimes(userId):
    talkUser = TalkTimes.objects.filter(userId=userId)[0]
    talkUser.residualTimes = int(talkUser.residualTimes) - 1
    talkUser.save()






