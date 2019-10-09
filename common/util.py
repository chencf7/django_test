# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import uuid
import xlrd
from datetime import date,datetime

'''
uuid1()：这个是根据当前的时间戳和MAC地址生成的，最后的12个字符408d5c985711对应的就是MAC地址
因为是MAC地址，那么唯一性应该不用说了。但是生成后暴露了MAC地址这就很不好了。
uuid3(p1, p2)：里面的namespace和具体的字符串都是我们指定的，然后呢···
应该是通过MD5生成的，这个我们也很少用到，莫名其妙的感觉。
uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的
但这就像中奖似的，几率超小，因为是随机而且使用还方便，所以使用这个的还是比较多的。
uuid5(p1, p2)：这个看起来和uuid3()貌似并没有什么不同，写法一样
也是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1.
'''
name = 'irp_web_uuid'
namespace = uuid.NAMESPACE_URL
def get_guid():
  uid = str(uuid.uuid5(namespace,name))
  return ''.join(uid.split('-'))

def read_excel(filename=""):
  # 文件名称出现中文字符时，读取文件报错， 需要进行编码
  '''
  Windows 下文件路径的中文编码是 GB2312/CP396，而 Python 设置编码为 UTF-8 ...
  所以应当对每一个文件路径做编码转换，就是先按照 GB2312 decode 然后再按照 UTF-8 encode..
  '''
  fn=unicode(filename, "utf8")
  wb=xlrd.open_workbook(filename=fn,encoding_override="utf-8")
  sheet1 = wb.sheet_by_index(0)
  trow=sheet1.nrows
  tcol=sheet1.ncols
  for i in range(0, trow):
    rows = sheet1.row_values(2) # 获取行内容
    for j in range(0, tcol):
      print(rows[j].decode('UTF-8').encode("gb2312"))
    break
  # cols = sheet1.col_values(3) # 获取列内容

