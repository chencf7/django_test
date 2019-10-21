#coding=utf-8
from __future__ import unicode_literals

from django.db import models
# import uuid

class Test(models.Model):
  name = models.CharField(max_length=20)

# class Person(models.Model):
#   id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, null=False)
#   name = models.CharField(max_length=6, null=False)
#   age = models.IntegerField()
#   time = models.DateTimeField(auto_now=True, null=False)
