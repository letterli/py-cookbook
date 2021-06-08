#! /usr/bin/env python
# _*_ coding: utf-8 _*_
#　二进制　八进制　十六进制　转换


# 将十六进制　八进制　二进制　转换成　十进制

print int('0x23', 16)
print int('023', 8)
print int('1111000', 2)


# 将　十进制　转换成　十六进制　八进制　二进制

print bin(120)
print oct(19)
print hex(120)


#　自定义函数实现转化

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        print base[rem]
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

print dec2hex(180)
