#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


HOST = 'smtp.qq.com'
FROM = '2339307889@qq.com'
TO = '420444983@qq.com'
SUBJECT = '官网业务服务质量周报'


def addimage(src, imgid):
    fp = open(src, 'rb')
    mimeImage = MIMEImage(fp.read())
    fp.close()
    mimeImage.add_header('Content-ID', imgid)
    return mimeImage


msg = MIMEMultipart('related')

msgtext = MIMEText("""<font color=red>官网业务周平均延时图表:<br><img src="cid:weekly" border="1"><br>详细内容见附件。</font>""","html","utf-8")

msg.attach(msgtext)
msg.attach(addimage('img/weekly.png', 'weekly'))


msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO

try:
     server = smtplib.SMTP()
     server.connect(HOST, 25)
     server.starttls()
     server.login(FROM, 'meljmopmnjfyebbb')
     server.sendmail(FROM, TO, msg.as_string())
     server.quit()
     print "邮件发送成功！"
except Exception, e:
     print "邮件发送失败："+str(e)





