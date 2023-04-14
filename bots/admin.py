from django.contrib import admin
from django.contrib.admin import ModelAdmin

from bots.models import TalkTimes, UsedOrder


# Register your models here.

class TalkTimesForAdmin(ModelAdmin):
    readonly_fields = ('id','userId','userName')
    search_fields = ['id','userId','userName']
    list_display = ('userId','userName','totleTimes','residualTimes')
admin.site.register(TalkTimes,TalkTimesForAdmin)
admin.site.register(UsedOrder)