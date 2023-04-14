#!/bin/bash

# 检查 celery worker 进程是否已经在运行
if ! pgrep -f "celery -A chatgpt worker -l info -P eventlet" > /dev/null; then
	    # 启动 celery worker 进程
	    cd /home/dev/chatgpt
	    celery -A chatgpt worker -l info -P eventlet &
		    echo "celery worker has been started."
	    else
		    echo "celery worker is already running."
fi
