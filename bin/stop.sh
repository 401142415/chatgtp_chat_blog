#!/bin/bash

# 关闭 Redis 服务
/usr/local/redis/src/redis-cli shutdown

# 关闭 Celery Worker 进程
pkill -f "celery -A chatgpt worker -l info -P eventlet"

echo "Redis and Celery have been stopped."

# 查找 Django 进程 ID
ps aux | grep 'python manage.py runserver' | awk '{print $2}' | xargs kill -9

echo "Django kill "
