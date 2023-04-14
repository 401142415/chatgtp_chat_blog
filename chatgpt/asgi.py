"""
ASGI config for chatgpt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
'''
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatgpt.settings')

application = get_asgi_application()
'''
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import bots.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatgpt.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # websocket请求使用的路由
    "websocket": AuthMiddlewareStack(
        URLRouter(
            bots.routing.websocket_urlpatterns
        )
    )
})