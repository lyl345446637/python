import requests
import numpy
from bs4 import BeautifulSoup
import time
import datetime
today2 = datetime.datetime.now()
c = str(today2)[11:19]
#新浪外原油数据接口
r = requests.get('https://gu.sina.cn/ft/api/jsonp.php/data=/GlobalService.getMink?symbol=CL&type=1').text
#s = BeautifulSoup(r.text)
sz = eval(r[55:-2]) #从字符转化为列表

i = sz[0] #设置一个变量测试
print(i['c']) #测试是否转化为列表 并取出一个列表
print(type(i['c'])) #看下数据类型

wlt = [] #新建一个变量
for i in sz: #循环取出要的每个列表的C值
    b = float(i['c']) #转化为浮点数
    wlt.append(b) #添加到wlt中

wlt300 = sum(wlt[-1:-301:-1]) / 300 #300均价
wlt150 = sum(wlt[-1:-151:-1]) / 150 #300均价
wlt100 = sum(wlt[-1:-101:-1]) / 100 #300均价
wlt50 = sum(wlt[-1:-51:-1]) / 50 #300均价


if wlt[-1] > wlt50 > wlt100 > wlt150 > wlt300 and wlt50 > wlt51:
    print('WTI'+'做多'+ '_'  + str(wlt[-1]) + '_' + c)
elif wlt300 > wlt150 > wlt100 > wlt50 > wlt[-1] and wlt50 < wlt51:
    print( 'WTI'+"做空"+ '_'  + str(wlt[-1]) + '_' + c)
else:
    print('WTI'+'震荡'+ '_'  + str(wlt[-1]) + '_' + c)

'''
wlxsun300 = sum(wint) / 300 #300均价
print(wlxsun300)
'''


