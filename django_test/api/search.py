# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
# import json

# from common import BaseResponse


# 表单
def search_page(request):
    return render_to_response('search/search_page.html')


# 接收请求数据
def search_result(request):
    request.encoding = 'utf-8'
    if 'searchtext' in request.GET and request.GET['searchtext']:
        message = '你搜索的内容为: ' + request.GET['searchtext']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
    # result = {"status":"错误","data":"","city":"北京"}
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    # return HttpResponse(BaseResponse.ok('成功'), content_type="application/json,charset=utf-8")
    # return BaseResponse.ok('成功')
