#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
from json import dumps
from threading import Thread
from base64 import b64encode


class FileTransferHandler(Thread):

    def __init__(self, cclient):
        super(FileTransferHandler, self).__init__()
        self.cclient = cclient

    def run(self):
        response_data = {}
        response_data['filename'] = 'beauty.jpg'
        response_data['filedata'] = data
        response_json_str = dumps(response_data)
        self.cclient.send(response_json_str.encode('utf-8'))
        self.cclient.close()

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(512)

    with open('beauty.jpg', 'rb') as f:
        data = b64encode(f.read().decode('utf-8'))

    while True:
        client, address = server.accept()
        print(str(address) + '连接到服务器！')
        FileTransferHandler(client).start()
