# -*- coding: utf-8 -*- 
import sys
# 输出系统默认编码，为ascii
# print(sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding("utf-8")
# 重置默认编码后，输出utf-8
# print(sys.getdefaultencoding())

import uuid
import xlrd
# 此处的路径需要参考调用本文件的main方法所在的路径
from entity.opgorg import *

'''
uuid1()：根据当前的时间戳和MAC地址生成，最后的12个字符对应的是MAC地址，确保唯一性，但会暴露MAC地址
uuid3(p1, p2)：里面的namespace和具体的字符串都是我们指定的，通过MD5生成的，比较少用到
uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的，随机重复几率很小
uuid5(p1, p2)：用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1
'''
name = 'irp_web_uuid'
namespace = uuid.NAMESPACE_URL
def get_guid():
  # uid = str(uuid.uuid5(namespace,name))
  uid = str(uuid.uuid4())
  return ''.join(uid.split('-'))

class Openexcel:
  def __init__(self, file_name='',sheet_id=0):
    # 如果传入参数，进行初始化出现异常的情况如何抛出错误
    self.filename=file_name
    self.sheetid=sheet_id

def read_excel(file_name='', sheet_id=0):
  fn = unicode(file_name, "utf8")
  wb = xlrd.open_workbook(filename=fn, encoding_override="utf-8")
  sheet1 = wb.sheet_by_index(sheet_id)
  trow = sheet1.nrows
  tcol = sheet1.ncols
  dttable = []
  for i in range(1, trow):
    print(sheet1.row_values(i)) # 获取行内容
    break


def read_excel_test(filename=""):
  # 文件名称出现中文字符时，读取文件报错， 需要进行编码
  """
  Windows 下文件路径的中文编码是 gbk/GB2312/CP396，而 Python 设置编码为 UTF-8 ...
  所以应当对每一个文件路径做编码转换，就是先按照 GB2312 decode 然后再按照 UTF-8 encode..
  """
  fn=unicode(filename, "utf8")
  wb=xlrd.open_workbook(filename=fn,encoding_override="utf-8")
  sheet1 = wb.sheet_by_index(0)
  trow=sheet1.nrows
  tcol=sheet1.ncols

  # 定义list
  org_list=[]
  for i in range(1, trow):
    prev_org = None
    rows = sheet1.row_values(i) # 获取行内容
    # 获取第7列内容，第7列为组织列
    # print(rows[7])
    org_name_arr = str(rows[7]).split('/')
    nlength=len(org_name_arr)
    for jk in range(0, nlength):
      # org_name=str(org_name_arr[jk]).decode('utf-8').encode('utf-8')
      org_name = str(org_name_arr[jk])

      existorg = []
      # 最后一项为岗位，若同一个组织下的岗位相同，则无需插入
      if jk==(nlength - 1):
        if not prev_org is None:
          lb_filter=lambda crt_org:crt_org.name==org_name and crt_org.parent==prev_org.id
          existorg=filter(lb_filter, org_list)
        else:
          pass
      else:
        existorg=filter(lambda crt_org:crt_org.name==org_name, org_list)
      if len(existorg)>0 and jk<(nlength - 1):
        prev_org=existorg[0]
      if len(existorg)==0:
        entity=Opgorg()
        entity.id=get_guid()
        entity.name=org_name
        if jk==(nlength - 1):
          entity.type=u'岗位'
        else:
          entity.type=u'组织'
        if prev_org is None:
          entity.syscode=entity.id+'.'
          entity.nodeleves=1
        else:
          entity.parent=prev_org.id
          entity.syscode=prev_org.syscode+entity.id+'.'
          entity.nodeleves=prev_org.nodeleves+1
        org_list.append(entity)
        prev_org=entity

    # for orgname in names:
    #   if(orgname not in org_list):
    #     org_list.append(orgname)
      
    # for j in range(0, tcol):
    #   # print(rows[j].decode('UTF-8').encode("gb2312"))
    #   print rows[j]
  # cols = sheet1.col_values(3) # 获取列内容
  # for jitm in org_list:
  #   print('~'.join(jitm.__dict__.values()))
  return org_list


# 判断对象数组是否存在某一项
# def list_isexist(list, _v):
#   flag=False
#   pass

