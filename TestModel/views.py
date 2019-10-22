# -*- coding: utf-8 -*-
# 模块中显式出现的所有字符串转为unicode类型
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.response import Response
import json
import uuid
# from models import Contact


# Create your views here.
def Hellotestmodel(request):
    return HttpResponse("hello testmodel")


def SaveContact(request):
    data = json.loads(request.body)
    data['id'] = uuid.uuid4()
    # res = {
    #   'success': True,
    #   'data': 'data is not null'
    # }
    # return Response(res)
    return HttpResponse("hello world")
