from django.db import models

# Create your models here.
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone


# 博客文章数据模型
class Article(models.Model):
    # 文章id,主键
    id = models.AutoField(primary_key=True)
    # 文章作者 ,用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题,models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 文章正文,保存大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间,参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间,参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

