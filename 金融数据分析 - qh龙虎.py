from jqdatasdk import *
import time
import datetime
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
#邮箱封装
def yx(sd):     
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

spqh = ['',''] #自己加品种

#基于聚宽平台的清洗数据封装
def lhbdkd(qqqqqq):
    today2 = datetime.datetime.now()  #今日时间
    yesterday = today2 - datetime.timedelta(days=1) #昨日时间
    tc = str(today2)[0:11]
    d = str(yesterday)[0:11]
    #上海期货交易所	XSGE
    #大连商品交易所	XDCE
    #郑州商品交易所	XZCE
    #中国金融期货交易所	CCFX
    sp = [qqqqqq] #,'BU2106.XSGE'
    dk = [501002 , 501003] # 501002-持买单量排名， 501003-持卖单量排名
    sj = [tc,d]
    auth('','')
    cc = []
    for k in sp:
        for i in dk:
            for t in sj:    
                # ID==501002-持买单量排名， 501003-持卖单量排名
                q=query(finance.FUT_MEMBER_POSITION_RANK.day,  #交易日
                        finance.FUT_MEMBER_POSITION_RANK.code, #合约编码
                        finance.FUT_MEMBER_POSITION_RANK.rank_type,
                        finance.FUT_MEMBER_POSITION_RANK.rank,
                        finance.FUT_MEMBER_POSITION_RANK.member_name,
                        finance.FUT_MEMBER_POSITION_RANK.indicator,
                finance.FUT_MEMBER_POSITION_RANK.indicator,).filter(finance.FUT_MEMBER_POSITION_RANK.code== k ,finance.FUT_MEMBER_POSITION_RANK.rank_type_ID== i,finance.FUT_MEMBER_POSITION_RANK.day == t ).order_by(finance.FUT_MEMBER_POSITION_RANK.day.desc()).limit(20)
                df=finance.run_query(q)
                b = df['indicator']
                c = sum(b) #多头持仓
                cc.append(c)
                #print(str(k) + '_' + str(c) +'-'+t)
                #先是多头数据  后 空头数据
    #print(cc)  排列 今日多头 昨日多头  今日空头  昨日空头
    fulhd = (cc[0] - cc[1]) / cc[1]
    fulhk = (cc[2] - cc[3]) / cc[3]
    dk = fulhd - fulhk
    if dk > 0:
        print(str(k)+'_'+'明日看多'+'_'+ str(tc)+'_'+ str(dk)[0:6])
        sd = str(k)+'_'+'明日看多'+'_'+ str(tc)+'_'+ str(dk)[0:6]
        yx(sd)
    else:
        print(str(k)+'_'+'明日看空'+'_'+ str(tc)+'_'+ str(dk)[0:6])
        sd = str(k)+'_'+'明日看空'+'_'+ str(tc)+'_'+ str(dk)[0:6]
        yx(sd)

#运行 -每晚19点后更新当日龙虎数据
for f in spqh:
    lhbdkd(f)