#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# description: 检测域名https证书过期时间
# author: letterli

import os
import datetime
import subprocess

domains = ['www.infzm.com','www.cmpassport.com']

for domain in domains:
    commad = subprocess.call('curl https://{0} --connect-timeout 10 -v -s -o /dev/null 2>/tmp/ca.info'.format(domain), shell=True)

    # 证书开始时间
    start_time = subprocess.check_output("cat /tmp/ca.info | grep 'start date: '", shell=True).decode('utf-8')
    # 证书到期时间
    end_time = subprocess.check_output("cat /tmp/ca.info | grep 'expire date: '", shell=True).decode('utf-8')
    # 证书颁发机构
    issuer = subprocess.check_output("cat /tmp/ca.info | grep 'issuer: '", shell=True).decode('utf-8')

    # 格式化时间
    format_start_time = '{0}:{1}:{2}'.format(start_time.split(':')[1].strip(), start_time.split(':')[2], start_time.split(':')[3]).strip()
    format_end_time = '{0}:{1}:{2}'.format(end_time.split(':')[1].strip(), end_time.split(':')[2], end_time.split(':')[3]).strip()

    expire_time = (datetime.datetime.strptime(format_end_time, '%a, %d %b %Y %H:%M:%S GMT') - datetime.datetime.strptime(format_start_time, '%a, %d %b %Y %H:%M:%S GMT')).days

    print('域名{0}证书还有 {1} 天过期.'.format(domain, expire_time))

    os.system('rm -f /tmp/ca.info')

