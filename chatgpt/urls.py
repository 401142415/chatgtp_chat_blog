"""chatgpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve

from article import views as article_views
import userprofile.views as userprofile_views
from django.urls import path, include, re_path

from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.urls import re_path

from bots import views


def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    # 博文管理
    # 这里的name，对于html中"{% url 'name' article.id %}" 的name
    path('list/', article_views.article_list, name='list'),  # 文章列表
    path('detail/<int:id>/', article_views.article_detail, name='detail'),
    path('create/', article_views.article_create, name='create'),
    path('delete/<int:id>/', article_views.article_delete, name='delete'),
    path('update/<int:id>/', article_views.article_update, name='update'),
    # 增加用户管理
    path('login/', userprofile_views.user_login, name='login'),
    path('logout/', userprofile_views.user_logout, name='logout'),
    path('register/', userprofile_views.user_register, name='register'),
    path('bots/', include('bots.urls')),

    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),  # 添加这行
    re_path(r'^$',  views.index),

]
