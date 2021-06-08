#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# pycurl 网络质量分析
# DNS解析-->TCP连接-->跳转【如有】-->SSL握手【如有】-->客户端准备-->服务器响应-->数据传输

import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

abuffer = BytesIO()

curl = pycurl.Curl()
curl.setopt(pycurl.ENCODING, "gzip")
curl.setopt(pycurl.URL, 'https://www.baidu.com/')    #指定请求的URL
curl.setopt(pycurl.WRITEDATA, abuffer)
curl.setopt(pycurl.CONNECTTIMEOUT, 10)    #连接的等待时间,设置为0则不等待
curl.setopt(pycurl.TIMEOUT, 10)  #最大下載时间
curl.setopt(pycurl.NOPROGRESS, 1)  #是否屏蔽下载进度条,非0则屏蔽
curl.setopt(pycurl.MAXREDIRS, 0)  #指定HTTP重定向的最大数
curl.setopt(pycurl.FORBID_REUSE, 1)  #完成交互后强制断开连接,不重用
curl.setopt(pycurl.FRESH_CONNECT, 1)     #强制获取新的连接,即替代缓存中的连接
curl.setopt(pycurl.DNS_CACHE_TIMEOUT, 1)    #设置保存DNS信息的时间,默认为120秒
curl.perform()

"""
* EFFECTIVE_URL             最终获取的url地址，尤其是当你指定给curl的地址存在301跳转，且通过-L继续追踪的情形。
* HTTP_CODE                 http状态码，如200成功,301转向,404未找到,500服务器错误等。
* TOTAL_TIME                总时间，按秒计。精确到小数点后三位。
* NAMELOOKUP_TIME           DNS解析时间,从请求开始到DNS解析完毕所用时间。
* CONNECT_TIME              连接时间,从开始到建立TCP连接完成所用时间,包括前边DNS解析时间，如果需要单纯的得到连接时间，用这个time_connect时间减去前边time_namelookup时间。
* APPCONNECT_TIME           连接建立完成时间，如SSL/SSH等建立连接或者完成三次握手时间。
* PRETRANSFER_TIME          从开始到准备传输的时间。
* REDIRECT_TIME             重定向时间，包括到最后一次传输前的几次重定向的DNS解析，连接，预传输，传输时间。
* REDIRECT_COUNT            重定向次数。
* SIZE_UPLOAD               上传大小。
* SIZE_DOWNLOAD             下载大小。
* SPEED_UPLOAD              上传速度,单位-字节每秒。 bytes/s
* HEADER_SIZE               下载的header的大小。
* REQUEST_SIZE              请求的大小。
* CONTENT_LENGTH_DOWNLOAD
* CONTENT_LENGTH_UPLOAD
* CONTENT_TYPE              text/html; charset=UTF-8
* RESPONSE_CODE             返回状态码
* SPEED_DOWNLOAD            下载速度，单位-字节每秒。
* SSL_VERIFYRESULT          ssl认证结果，返回0表示认证成功。
* INFO_FILETIME
* STARTTRANSFER_TIME        开始传输时间。在发出请求之后，Web 服务器返回数据的第一个字节所用的时间。
* HTTP_CONNECTCODE
* HTTPAUTH_AVAIL
* PROXYAUTH_AVAIL
* OS_ERRNO
* NUM_CONNECTS
* SSL_ENGINES
* INFO_COOKIELIST
* LASTSOCKET
* FTP_ENTRY_PATH
"""

meta = {}
meta['effective-url'] = curl.getinfo(pycurl.EFFECTIVE_URL)
meta['http-code'] = curl.getinfo(pycurl.HTTP_CODE)
meta['total-time'] = curl.getinfo(pycurl.TOTAL_TIME)
meta['namelookup-time'] = curl.getinfo(pycurl.NAMELOOKUP_TIME)
meta['connect-time'] = curl.getinfo(pycurl.CONNECT_TIME)
meta['pretransfer-time'] = curl.getinfo(pycurl.PRETRANSFER_TIME)
meta['redirect-time'] = curl.getinfo(pycurl.REDIRECT_TIME)
meta['redirect-count'] = curl.getinfo(pycurl.REDIRECT_COUNT)
meta['size-upload'] = curl.getinfo(pycurl.SIZE_UPLOAD)
meta['size-download'] = curl.getinfo(pycurl.SIZE_DOWNLOAD)
meta['speed-upload'] = curl.getinfo(pycurl.SPEED_UPLOAD)
meta['header-size'] = curl.getinfo(pycurl.HEADER_SIZE)
meta['request-size'] = curl.getinfo(pycurl.REQUEST_SIZE)
meta['content-length-download'] = curl.getinfo(pycurl.CONTENT_LENGTH_DOWNLOAD)
meta['content-length-upload'] = curl.getinfo(pycurl.CONTENT_LENGTH_UPLOAD)
meta['content-type'] = curl.getinfo(pycurl.CONTENT_TYPE)
meta['response-code'] = curl.getinfo(pycurl.RESPONSE_CODE)
meta['speed-download'] = curl.getinfo(pycurl.SPEED_DOWNLOAD)
meta['ssl-verifyresult'] = curl.getinfo(pycurl.SSL_VERIFYRESULT)
meta['filetime'] = curl.getinfo(pycurl.INFO_FILETIME)
meta['starttransfer-time'] = curl.getinfo(pycurl.STARTTRANSFER_TIME)
meta['redirect-time'] = curl.getinfo(pycurl.REDIRECT_TIME)
meta['redirect-count'] = curl.getinfo(pycurl.REDIRECT_COUNT)
meta['http-connectcode'] = curl.getinfo(pycurl.HTTP_CONNECTCODE)
meta['httpauth-avail'] = curl.getinfo(pycurl.HTTPAUTH_AVAIL)
meta['proxyauth-avail'] = curl.getinfo(pycurl.PROXYAUTH_AVAIL)
meta['os-errno'] = curl.getinfo(pycurl.OS_ERRNO)
meta['num-connects'] = curl.getinfo(pycurl.NUM_CONNECTS)
meta['ssl-engines'] = curl.getinfo(pycurl.SSL_ENGINES)
meta['cookielist'] = curl.getinfo(pycurl.INFO_COOKIELIST)
meta['lastsocket'] = curl.getinfo(pycurl.LASTSOCKET)
meta['ftp-entry-path'] = curl.getinfo(pycurl.FTP_ENTRY_PATH)
meta['time_appconnect'] = curl.getinfo(pycurl.APPCONNECT_TIME)


total_time = curl.getinfo(pycurl.TOTAL_TIME)             #传输结束所消耗的总时间
dns_time = curl.getinfo(pycurl.NAMELOOKUP_TIME)          #从发起请求到DNS解析完成所消耗的时间
connect_time = curl.getinfo(pycurl.CONNECT_TIME)         #从发起请求到建立连接所消耗的时间
redirect_time = curl.getinfo(pycurl.REDIRECT_TIME)       #从发起请求到重定向所消耗的时间
ssl_time = curl.getinfo(pycurl.APPCONNECT_TIME)          #从发起请求到SSL建立握手时间
pretrans_time = curl.getinfo(pycurl.PRETRANSFER_TIME)    #从发起请求到准备传输所消耗的时间
starttrans_time = curl.getinfo(pycurl.STARTTRANSFER_TIME)#从发起请求到接收第一个字节的时间
print '发起请求到DNS解析时间 : %.3f ms' %(dns_time*1000)
print '发起请求到TCP连接完成时间: %.3f ms' %(connect_time*1000)
print '发起请求到跳转完成时间: %.3f ms' %(redirect_time*1000)
print '发起请求到SSL建立完成时间 : %.3f ms' %(ssl_time*1000)
print '发起请求到客户端发送请求时间： %.3f ms' %(pretrans_time*1000)
print '发起请求到客户端接受首包时间: %.3f ms' %(starttrans_time*1000)
print '总时间为: %.3f ms' %(total_time*1000)
print ''

transfer_time = total_time - starttrans_time   #传输时间
serverreq_time = starttrans_time - pretrans_time  #服务器响应时间，包括网络传输时间
if ssl_time == 0 :
    if redirect_time == 0 :
        clientper_time = pretrans_time - connect_time #客户端准备发送数据时间
        redirect_time = 0
    else :
        clientper_time = pretrans_time - redirect_time
        redirect_time = redirect_time - connect_time
    ssl_time = 0
else :
    clientper_time = pretrans_time - ssl_time
    if redirect_time == 0 :
        ssl_time = ssl_time - connect_time
        redirect_time = 0
    else :
        ssl_time = ssl_time - redirect_time
        redirect_time = redirect_time - connect_time
connect_time = connect_time - dns_time

print '发起请求到DNS解析时间 : %.3f ms' %(dns_time*1000)
print 'TCP连接消耗时间 : %.3f ms' %(connect_time*1000)
print '跳转消耗时间: %.3f ms' %(redirect_time*1000)
print 'SSL握手消耗时间 : %.3f ms' %(ssl_time*1000)
print '客户端发送请求准备时间: %.3f ms' %(clientper_time*1000)
print '服务器处理时间: %.3f ms' %(serverreq_time*1000)
print '数据传输时间: %.3f ms' %(transfer_time*1000)

curl.close()
