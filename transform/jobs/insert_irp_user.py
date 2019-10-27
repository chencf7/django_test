# -*- coding: utf-8 -*- 
import MySQLdb
import uuid
import xlrd
from datetime import date,datetime

import sys
import os
# print(os.getcwd()) # C:\Code\django_test
# print(os.path.abspath('..')) # C:\Code
# cpath="%s%s"%(os.getcwd(),"\common")
# sys.path.append(cpath)
sys.path.append(os.getcwd())
from common import util

# 文件为中文名编码会造成读取文件报错
# filepath=r'C:\Code\django_test\transform\data\jg_副本.xls'
# fp="%s%s"%(os.getcwd(),r'\transform\data\jg_副本.xls')
fp="%s%s"%(r'C:\Code\django_test',r'\transform\data\jg_副本.xls')
def insertdata2db():
  rlist=util.read_excel(fp)
  return 0
  # executemany写sql不管什么类型，统一使用%s作为占位符
  # %s不需要引号
  sqlstr='''insert into opgorg(`id`,name,parent,syscode,nodeleves,type,dr,createtime) 
  values(%s,%s,%s,%s,%s,%s,%s,%s)'''

  dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  args_tup = [(itm.id,itm.name,itm.parent,itm.syscode,itm.nodeleves,itm.type,0,dt)
              for itm in rlist]
  # args_tup=(('12','2','3','4','5','6'),('11','21','31','41','51','61'))
  db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="dhcc",db="irp_web",port=3306,charset='utf8')
  cursor = db.cursor()
  try:
    # 参数args_tup可为数组（内部为元组），也可为元组（内部仍为元组）
    cursor.executemany(sqlstr,args_tup)
    db.commit()
  except Exception as e:
    db.rollback()
  db.close()
  return 0

  db=MySQLdb.connect("127.0.0.1","root","dhcc","irp_web")
  cursor=db.cursor()
  guid = util.get_guid()
  sql="insert into irp_user(id, code, name, idcard)\
      values(%s, '2523', '1523333', '429959291')" % guid
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