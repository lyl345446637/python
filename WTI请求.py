import requests
import numpy
from bs4 import BeautifulSoup
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
wlt300 = wlt[-1:-301:-1] #只要最新的300个数据

sunwlt300 = sum(wlt300) / 300 #300均价
print(sunwlt300) 



'''
wlxsun300 = sum(wint) / 300 #300均价
print(wlxsun300)
'''


