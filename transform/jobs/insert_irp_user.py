# -*- coding: utf-8 -*- 
import MySQLdb
import uuid
import xlrd
from datetime import date,datetime

import sys
import os
# print(os.getcwd()) # C:\Code\django_test
# print(os.path.abspath('..')) # C:\Code
cpath="%s%s"%(os.getcwd(),"\common")
sys.path.append(cpath)
import util

# 文件为中文名编码会造成读取文件报错
# filepath=r'C:\Code\django_test\transform\data\jg_副本.xls'
fp="%s%s"%(os.getcwd(),r'\transform\data\jg_副本.xls')
def insertdata2db():
  util.read_excel(fp)
  return 0

  db=MySQLdb.connect("127.0.0.1", "root", "dhcc", "irp_web")
  cursor=db.cursor()
  guid = util.get_guid()
  sql="insert into irp_user(id, code, name, idcard)\
      values('%s', '2523', '1523333', '429959291')"%(guid)
  try:
    cursor.execute(sql)
    db.commit()
  except Exception as e:
    db.rollback()
  db.close()



'''
Python不同于C/C++，程序执行并不需要主程序，如main()，而是文件自上而下的执行。
但很多Python程序中都有
if __name__ == '__main__':
  statements
这样的语句。
这段代码的主要作用主要是让该python文件既可以独立运行，也可以当做模块导入到其他文件。
当导入到其他的脚本文件的时候，此时__name__的名字其实是导入模块的名字，不是’__main__’, main代码里面的就不执行了。
'''
if __name__=='__main__':
  insertdata2db()
  print 'main func'