# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test

# Register your models here.
# class PersonAdmin(admin.ModelAdmin):
#   # 管理可见字段
#   list_display=['id', 'name', 'age', 'time']

admin.site.register(Test)

# from TestModel.models import Test,Contact,Tag

# # Register your models here.
# admin.site.register([Test, Contact, Tag])
