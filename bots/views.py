import asyncio

from django.contrib.auth.decorators import login_required
# bots/views.py
from django.shortcuts import render



@login_required(login_url='/login/')
def index(request):
    context={"user":request.user}
    return render(request, 'bots/index.html', context)