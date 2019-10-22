# coding=utf-8
"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# 2.7.x版本的django不支持path
# from django.urls import path
from django.contrib import admin

from . import view
from api import search

import TestModel.urls

urlpatterns = [
    # 默认管理工具路由
    url(r'^admin/', admin.site.urls),

    # 正则表达式，以^开头，以$结束
    # url(r'^$', view.hello),
    url(r'^hello$', view.hello),
    url(r'^hello_tpl$', view.hello_tpl),
    url(r'^search$', search.search_page),
    url(r'^result$', search.search_result),

    url(r'^testmodel/', include(TestModel.urls)),
]
