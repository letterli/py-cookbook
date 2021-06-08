#! /usr/bin/env python
# _*_ coding: utf-8 _*_
'''
IP地址处理模块
'''

from IPy import IP

ip_s = raw_input('Please input an IP or net-range:')
ips = IP(ip_s)

if len(ips) > 1:
    print 'net: %s' % ips.net()
    print 'netmask: %s' % ips.netmask()
    print 'broadcast: %s' % ips.broadcast()
    print 'reverse address: %s' % ips.reverseNames()[0]
    print 'subnet: %s' % len(ips)
else:
    print 'reverse address: %s' % ips.reverseNames()[0]


ip = IP('192.168.1.0/24')

print ip.net()
print ip.int()
print ip.version()
print ip.broadcast()
print ip.prefixlen()
print ip.strBin()
print ip.iptype()
print ip.netmask()
print ip.reverseNames()







