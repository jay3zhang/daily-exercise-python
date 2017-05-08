# coding=utf-8
'''
获取当天的就业信息，
发送邮件提醒，一则消息发一封邮件
发送微信提醒
'''

import requests
import re
import time
from bs4 import BeautifulSoup
# 发送邮件需要的模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_today_link():
    # 抓取当日信息的链接
    today_list=[]   #存放当日消息的相对链接

    url = 'http://ssdut.dlut.edu.cn/bkspy/bksgl/zsjy.htm'    #ssdut的就业页面
    r = requests.get(url)
    r.encoding = 'utf-8'
    # print(r.status_code)
    soup = BeautifulSoup(r.text,'html.parser')
    # 抓取链接和时间
    divs = soup.find_all('div', attrs={'class':'mt_10 mb_10'})
    for div in divs:
        link = div.span.a.attrs['href'].split('/',2)[2]
        time = re.findall(r'\d+-\d+-\d+', div.text, re.S)[0]    # type(time)=str，这个标签下文字有点乱所以用了re模块，也可用split()切割两次
        # print(link,time)
        if time==ctime:
            today_list.append(link)
    return today_list

def get_today_message(link_list):
    baseURL = 'http://ssdut.dlut.edu.cn/'
    message=[]
    if len(link_list)==0:
        # 链接为空，没消息，返回空列表
        return message
    for link in link_list:
        mess_url = baseURL+link
        # print(mess_url)
        mess_r = requests.get(mess_url)
        mess_r.encoding = 'utf-8'
        # print(r.status_code)
        mess_soup = BeautifulSoup(mess_r.text, 'html.parser')
        page={}
        page['title']=mess_soup.h1.string
        page['content'] = mess_soup.find('div', attrs={'id':'vsb_content'}).text   # 本来要做内容清理，测试了下内容很干净，不用清理
        page['link'] = mess_url
        page['date'] = ctime
        message.append(page)

    return message

import email_account    # 邮件发送着信息
import email_list    # 邮件接收者列表
def send_email(message):
    smtpserver = 'smtp.163.com'  # 发送者的邮箱服务器
    user = email_account.username
    password = email_account.password
    sender = email_account.username  # 发送者

    # 编写邮件正文
    if len(message)==0:
        msg = MIMEText('', 'html', 'utf-8')
        msg['Subject'] = Header(ctime+'无消息', 'utf-8')
    else:
        text = '标题：'+'\t'+message.get('title')+'\n' + message.get('date') +\
                '正文：'+'\n'+message.get('content')+'\n' +\
            '原文链接：'+'\t'+message.get('link')

        msg = MIMEText(text, 'plain', 'utf-8')
        msg['Subject'] = Header(message.get('title'), 'utf-8')
    # 必须有这两个参数，否则网易邮箱会视为垃圾邮件，拒发
    msg['From'] = sender
    # msg['To'] = receiver

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    for receiver in email_list.to_list:
        msg['To'] = receiver
        smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

from wxpy import *
bot = Bot(cache_path=True)
def wechat_notice(message):
    # 机器人账号自身
    myself = bot.self

    # 构建wechat要发送的信息
    msg = message.get('title')+'\n'+message.get('date')+'\n'+message.get('link')

    # 向文件传输助手发送消息
    bot.file_helper.send(msg)

    # 查找群聊
    to_group = bot.groups().search('陆壹伍')
    if to_group:
        # print(to_group)
           ## 发送群聊消息
        to_group[0].send_msg(msg)

    # embed()
    # bot.join()  #进程应该在调用函数中阻塞，否则后面的消息发送

def send():
    today_link = get_today_link()
    message = get_today_message(today_link)
    # 没有消息不发送邮件
    if message:
        print(len(message))
        for item in message:
            # send_email(item)
            wechat_notice(item)

    bot.join()  # 堵塞bot线程，持续监听

if __name__=='__main__':
    #定时任务
    while True:
        # 获取当日时间    str类型
        ctime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # ctime = '2017-04-28'
        # print(ctime)
        current_time = time.localtime(time.time())
        time1 = (current_time.tm_hour == 12) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)
        time2 = (current_time.tm_hour == 18) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)
        ## time2 = True
        if (time1 or time2):
            send()
        time.sleep(2)
