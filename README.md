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

* win10手动创建.gitignore文件
直接命名报错
1. 在项目根目录下面创建 gitignore.txt 文件,你也可以使用任意的名字来命名。
2. 右键选择 Git Bash , 调出 Git 命令行。
3. 输入 mv gitignore.txt .gitignore 即可。
4. 编辑 .gitignore 添加规则即可。
