# coding=utf-8
from django.http import JsonResponse, HttpResponse


class Httpcode(object):
    '''
    定义状态
    '''
    ok = 200
    error = 400
    noauth = 401
    notfound = 404
    methoderr = 405
    servererr = 500


def BaseResponse(code=Httpcode.ok, message='', data=None, kwargs=None):
    '''
    封装返回JsonResponse方法
    :param code:  状态
    :param message:  错误信息
    :param data:  返回数据
    :param kwargs:  保证代码的健壮性
    :return: JsonResponse数据
    '''
    # 定义返回的字典
    jsonresult = {'data': data, 'code': code, 'message': message}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        jsonresult.update(kwargs)
    return JsonResponse(jsonresult, json_dumps_params={'ensure_ascii': False})


def ok(data=None):
    result = BaseResponse(code=Httpcode.ok, message='ok', data=data)
    return HttpResponse(result, content_type="application/json,charset=utf-8")


def error(data=None, message=''):
    return BaseResponse(code=Httpcode.error, message=message, data=data)
