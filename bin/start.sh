cd /home/dev/chatgpt/bin
nohup sh redis_start.sh >> ../logs/redis.log &

nohup sh celery_start.sh >> ../logs/celery.log &

cd ..
nohup python manage.py runserver 0.0.0.0:8000 >> logs/chatgpt.log &

