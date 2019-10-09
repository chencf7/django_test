from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
  return HttpResponse("hello world")

def hello_tpl(req):
  context={}
  context['hello']='hello template'
  return render(req, 'hello.html', context)