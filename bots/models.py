from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# 聊天次数记录
class TalkTimes(models.Model):
    # 次数id,主键
    id = models.AutoField(primary_key=True,verbose_name="序号")
    # 用户主键id
    userId = models.IntegerField(verbose_name="用户id",default=None)
    # 用户名
    userName = models.CharField(max_length=100,verbose_name="用户名")
    # 总次数
    totleTimes = models.IntegerField(verbose_name="总次数",default=0,
                                     validators=[MaxValueValidator(1000), MinValueValidator(0)])
    # 剩余次数
    residualTimes = models.IntegerField(verbose_name="剩余次数",default=0,
                                     validators=[MaxValueValidator(1000), MinValueValidator(0)])

# 已用订单
class UsedOrder(models.Model):
    # 次数id,主键
    id = models.AutoField(primary_key=True,verbose_name="序号")
    # 用户主键id
    userId = models.CharField(max_length=30,verbose_name="订单号")