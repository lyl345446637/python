import requests
import numpy
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import time
import datetime
def yx(sd):     
    today3 = datetime.datetime.now()
    msg_from = '345446637@qq.com'  # 发送方邮箱
    passwd = ''   #就是上面的授权码
    to = ['345446637@qq.com'] #接受方邮箱

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
def wti():
    #新浪外原油数据接口
    r = requests.get('https://gu.sina.cn/ft/api/jsonp.php/data=/GlobalService.getMink?symbol=CL&type=5').text
    #s = BeautifulSoup(r.text)
    sz = eval(r[55:-2]) #从字符转化为列表

    i = sz[0] #设置一个变量测试
    '''
    print(i['c']) #测试是否转化为列表 并取出一个列表
    print(type(i['c'])) #看下数据类型
    '''

    wlt = [] #新建一个变量
    for i in sz: #循环取出要的每个列表的C值
        b = float(i['c']) #转化为浮点数
        wlt.append(b) #添加到wlt中

    wlt1000 = sum(wlt[-1:-1001:-1]) /1000 #只要最新的300个数据
    wlt800 = sum(wlt[-1:-801:-1]) /800 #只要最新的300个数据
    wlt600 = sum(wlt[-1:-601:-1]) /600 #只要最新的300个数据
    wlt400 = sum(wlt[-1:-401:-1]) /400 #只要最新的300个数据

    wlt1002 = sum(wlt[-2:-1002:-1]) /1000 #只要最新的300个数据
    wlt802 = sum(wlt[-2:-802:-1]) /800 #只要最新的300个数据
    wlt602 = sum(wlt[-2:-602:-1]) /600 #只要最新的300个数据
    wlt402 = sum(wlt[-2:-402:-1]) /400 #只要最新的300个数据


    if wlt[-1] > wlt1000:
        if wlt[-2] <= wlt1002:
            sd = 'WTI' + '_'+ "5000开多" + '_' + str(wlt[-1])
            yx(sd)
    elif wlt[-1] > wlt800:
        if wlt[-2] <= wlt802:
            sd = 'WTI' + '_'+ "4000开多" + '_' + str(wlt[-1])
            yx(sd)
    elif wlt[-1] > wlt600:
        if wlt[-2] <= wlt602:
            sd = 'WTI' + '_'+ "3000开多" + '_' + str(wlt[-1])
            yx(sd)
    elif wlt[-1] > wlt400:
        if wlt[-2] <= wlt402:
            sd = 'WTI' + '_'+ "2000开多" + '_' + str(wlt[-1])
            yx(sd)

    if wlt[-1] < wlt1000:
        if wlt[-2] >= wlt1002:
            sd = 'WTI' + '_'+ "5000开空" + '_' + str(wlt[-1])
            yx(sd)
    elif wlt[-1] < wlt800:
        if wlt[-2] >= wlt802:
            sd = 'WTI' + '_'+ "4000开空" + '_' + str(wlt[-1])
            yx(sd)
    elif wlt[-1] < wlt600:
        if wlt[-2] >= wlt602:
            sd = 'WTI' + '_'+ "3000开空" + '_' + str(wlt[-1])
            yx(sd)
    elif wlt[-1] < wlt400:
        if wlt[-2] >= wlt402:
            sd = 'WTI' + '_'+ "2000开空" + '_' + str(wlt[-1])
            yx(sd)
    v = datetime.datetime.now()
    print(str(wlt[-1])+'_'+str(v)[11:19])
while 1>0:
    wti()
    time.sleep(300.01)             
