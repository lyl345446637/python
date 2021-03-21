from jqdatasdk import *
import time
import datetime

#数据来源聚宽
auth('账号','密码')
'''
is_auth = is_auth()
print(is_auth) #是否连接上服务器
count = get_query_count()
print(count) #查看剩余获取条数
'''

while 1 > 0:
    today2 = datetime.datetime.now()
    c = str(today2)[11:19]
    while '08:59:00' < c < '11:31:00' or '13:29:00' < c < '15:31:00' or '20:59:00' < c < '23:01:00':
        today = datetime.datetime.now()
        hg = ['BU','FU','SC','LU']
        for i in hg:
            df = get_dominant_future( i ,today)

            hgl = get_price(df,
                        end_date=today,
                        frequency='minute', 
                        fields=None, 
                        skip_paused=False, 
                        fq='pre', 
                        count=0,
                        panel=True, 
                        fill_paused=True)
                        
            hgsum = hgl['close'] #列表进行存储

            hg0 = sum(hgsum) /  0   #列表进行300运算
            hg0 = sum(hgsum[-1:-2:-1]) /  0   #列表进行0运算
            hg1 = sum(hgsum[-2:-3:-1]) /  0     #列表进行0-1运算

            if str(i)== 'BU' :
                i = '沥青'
            elif str(i)== 'FU' :
                i = '燃油'
            elif str(i)== 'SC' :
                i = '原油'
            elif str(i)== 'LU' :
                i = '低硫'

            if hgsum[-1] > hg300 and hg50 > hg51:
                print( i + '_' + '做多' + str(hgsum[-1]))
            elif hg300 > hgsum[-1] and hg50 < hg51:
                print(i + '_' + "做空" + str(hgsum[-1]))
            else:
                print(i + '_' + '震荡' + str(hgsum[-1]))
            
        time.sleep(60.01)
        break




