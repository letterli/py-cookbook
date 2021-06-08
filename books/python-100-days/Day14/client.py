#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器
    client.connect(('localhost', 8080))
    # 3.接收服务器数据
    print(str(client.recv(1024)).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()

