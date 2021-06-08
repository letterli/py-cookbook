#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import smtplib
import string


HOST = 'smtp.qq.com'
SUBJECT = 'Test email form Python'
TO = '420444983@qq.com'
FROM = '2339307889@qq.com'
TEXT = 'Python rules then all!'
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        TEXT
        ), "\r\n")

server = smtplib.SMTP('smtp.qq.com', 25)
server.starttls()
server.login('2339307889@qq.com', 'meljmopmnjfyebbb')
server.sendmail(FROM, [TO], BODY)
server.quit()


