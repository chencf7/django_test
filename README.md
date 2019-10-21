##### django框架

##### 初始化django框架
1. 开发环境python2.7+django1.11.24
2. 创建项目
django-admin startproject xxx
3. 创建app
python manage.py startapp xxx
4. 启动项目
python manage.py runserver 127.0.0.1:8000
或者使用vscode直接调试启动即可

##### django框架
1. 设置整个框架下解码为utf-8，避免每个文件头设置#coding=utf-8
在settings.py文件内添加内容
```python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
```
2. BaseResponse.py（common目录下）
封装返回的json格式

3. python编码格式的问题
```python
import sys
print(sys.getdefaultencoding()) # 打印当前系统默认编码
```
* python中utf-8与gbk/gb2312转换，需要通过unicode/ascii做为中介
* utf-8转gbk，通过decode解码为unicode，再通过encode编码为gbk；xxx.decode("utf-8").encode("gbk")
* gbk转utf-8类似
* windows系统最好以utf-8的编码输出，不会有乱码

##### django模型（models）
1. python manage.py startapp xxx或者命令django-admin startapp xxx
2. 在django_test目录下的setting中注册app
```python
INSTALLED_APPS = [
  ...
  # 添加创建的app，python manage.py makemigrations时才能自动创建models
  'TestModel'
]
```
3. 在新建app目录下的models.py文件内添加需要的插入的类
> 不能在默认启动app，django_test下直接创建models.py，使用makemigrations命令时，无法detected到
4. 依次执行命令
+ # python manage.py migrate   # 创建表结构
+ python manage.py makemigrations xxx  # 让 Django 知道我们在我们的模型有一些变更
+ python manage.py migrate xxx   # 创建表结构


##### django后台管理工具
1. 在启动app中的urls.py中查看是否有配置后台管理工具的url
+ url(r'^admin/', admin.site.urls),
2. 后台管理工具添加超级管理员admin
python manage.py createsuperuser
3. 修改用户
python manage.py changepassword admin
4. 使用admin后台管理工具管理模型
+ 需要注册模型到admin
> eg:  TestModel 中已经创建了模型 Test 。修改 TestModel/admin.py:
> ```python
> from TestModel.models import Test
> # Register your models here.
> admin.site.register(Test)
> ```

