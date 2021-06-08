#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import dns.resolver


# 将域名转换成ｉｐ地址
domain = raw_input('Please input an domain: ')

A = dns.resolver.query(domain, 'A')

for i in A.response.answer:
    for j in i.items:
        print j.address


# 邮件交换记录，定义邮件服务器的域名
mx_domain = raw_input('Please input an domain: ')

MX = dns.resolver.query(mx_domain, 'MX')

for i in MX:
    print 'MX preference =', i.preference, 'mail exchanger =', i.exchange


#　别名记录，实现域名间的映射
ns_domain = raw_input('Please input an domain: ')

ns = dns.resolver.query(ns_domain, 'NS')

for i in ns.response.answer:
    for j in i.items:
        print j.to_text()


# 标记区域的域名服务器及授权子域
cname_domain = raw_input('Please input an domain: ')

cname = dns.resolver.query(cname_domain, 'CNAME')

for i in cname.response.answer:
    for j in i.items:
        print j.to_text()
