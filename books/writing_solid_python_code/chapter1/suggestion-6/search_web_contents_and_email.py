#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description: 获取网页内容、查找指定网页内容、发送邮件


import requests
import smtplib


def getWebContents(url):
    headers = {
        'accept': 'text/html',
        'user-agent': 'python 2.7'
    }
    response = requests.get(url, headers=headers)
    return response.text


def search(webcontent, start_line, end_line):
    lines = webcontent.splitlines()
    return lines[start:end]


def send_email(sender, receiver, smtpserver, username, password, content):
    subject = "Contented get from the web"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    getWebContents('http://www.infzm.com')
