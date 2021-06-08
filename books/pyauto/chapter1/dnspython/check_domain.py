#! /usr/bin/env python
# _*_ coding: utf-8 _*_

"""DNS域名轮循业务监控"""

import dns.resolver
# 一个相对底层的http请求模块
import httplib


def get_iplist(domain=''):
    iplist = []
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception, e:
        print 'dns resolver error : ' + str(e)
        return

    for i in A.response.answer:
        for j in i.items:
            print(j)
    #         iplist.append(j.address)
    # return iplist


def check_ip(ip):
    checkurl = ip + ':80'
    httplib.socket.setdefaulttimeout(5)
    connect = httplib.HTTPConnection(checkurl)

    try:
        connect.request('GET', '/')
        r = connect.getresponse()
        getcontent = r.read(15)
    except Exception, e:
        print 'http request error'
    finally:
        connect.close()
        if getcontent == '<!DOCTYPE html>':
            print ip + ' [OK]'
        else:
            print ip + ' [Error]'


if __name__ == '__main__':
    domain = 'www.infzm.com'
    iplist = get_iplist(domain)

    # if len(iplist) > 0:
    #     for ip in iplist:
    #         check_ip(ip)
    # else:
    #     print 'dns resolver error.'
