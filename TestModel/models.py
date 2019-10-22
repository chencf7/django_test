# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = u"测试表"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    # 打印美化，直接print对象实列时调用此方法
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
