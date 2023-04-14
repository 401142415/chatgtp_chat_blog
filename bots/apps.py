from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class BotsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bots'
"""
    def ready(self):
        print("xrf reday")
        autodiscover_modules("bot.py")
        print("xrf ready end")
"""