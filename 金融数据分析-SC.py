from jqdatasdk import *
import time
import datetime
#发送多种类型的邮件
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
def yx(sd):#邮箱封装 
    today3 = datetime.datetime.now()
    msg_from = ''  # 发送方邮箱
    passwd = ''   #就是上面的授权码
    to = [''] #接受方邮箱

    #设置邮件内容
    #MIMEMultipart类可以放任何内容
    msg = MIMEMultipart()
    conntent= str(today3)
    #把内容加进去
    msg.attach(MIMEText(conntent,'plain','utf-8'))

    #设置邮件主题
    msg['Subject']= str(sd)

    #发送方信息
    msg['From']=msg_from

    #开始发送

    #通过SSL方式发送，服务器地址和端口
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 登录邮箱
    s.login(msg_from, passwd)
    #开始发送
    s.sendmail(msg_from,to,msg.as_string())
    print("邮件发送成功")                                                       

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
    while '08:59:00' < c < '11:31:00' or '13:29:00' < c < '15:01:00' or '20:59:00' < c < '23:01:00':
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
                        count=305, 
                        panel=True, 
                        fill_paused=True)
                        
            hgsum = hgl['close'] #列表进行存储

            hg300 = sum(hgsum[-1:-301:-1]) / 300   #列表进行300运算
            hg150 = sum(hgsum[-1:-151:-1]) / 150   #列表进行150运算
            hg100 = sum(hgsum[-1:-101:-1]) / 100   #列表进行100运算
            hg50 = sum(hgsum[-1:-51:-1]) / 50     #列表进行50运算

            hg301 = sum(hgsum[-2:-302:-1]) / 300   #列表进行301运算
            hg151 = sum(hgsum[-2:-152:-1]) / 150   #列表进行151运算
            hg101 = sum(hgsum[-2:-102:-1]) / 100   #列表进行101运算
            hg51 = sum(hgsum[-2:-52:-1]) / 50     #列表进行51运算

            if str(i)== 'BU' :
                i = '沥青'
            elif str(i)== 'FU' :
                i = '燃油'
            elif str(i)== 'SC' :
                i = '原油'
            elif str(i)== 'LU' :
                i = '低硫'
            
            if hgsum[-1] > hg50 > hg100 > hg150 > hg300 and hg50 > hg51:
                print( i + '_' + '做多' + str(hgsum[-1]))
            elif hg300 > hg150 > hg100 > hg50 > hgsum[-1] and hg50 < hg51:
                print(i + '_' + "做空" + str(hgsum[-1]))
            else:
                print(i + '_' + '震荡' + str(hgsum[-1]))
            
            sd = ''
            if hg50 > hg300:
                if hg51 <= hg301:
                    sd = "准备转-多"
                    yx(sd)
                elif hgsum[-1] < hg50:
                    if hgsum[-2] > hg51:
                        sd = "空震荡"
                        yx(sd)
            
            if hg50 < hg300:
                if hg51 >= hg301:
                    sd = "准备转-空"
                    yx(sd)
                elif hgsum[-1] > hg50:
                    if hgsum[-2] < hg51:
                        sd = "空震荡"
                        yx(sd)
        time.sleep(60.01)
        break