##### django框架

* 初始化django框架
1. 开发环境python2.7+django1.11.24
2. 创建项目
django-admin startproject xxx
3. 创建app
python manage.py startapp xxx
4. 启动项目
python manage.py runserver 0.0.0.0:8000
或者使用vscode直接调试启动即可

* django框架封装
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