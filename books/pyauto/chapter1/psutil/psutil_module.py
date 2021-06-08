#! /usr/bin/env python
# _*_ coding: utf-8 _*_
'''
系统性能信息模块
'''

import psutil


# cpu infomation

print psutil.cpu_times()                  # 获取cpu完整信息

# output
# scputimes(user=227.12, nice=64.93, system=251.94, idle=17735.12, iowait=379.88, irq=0.0, softirq=18.13, steal=0.0, guest=0.0, guest_nice=0.0)

print psutil.cpu_times().user              # 获取user的cpu时间比
print psutil.cpu_count()                   # 获取cpu逻辑个数
print psutil.cpu_count(logical = False)    # 获取cpu物理个数


# memery infomation

print psutil.virtual_memory().total

# output
# svmem(total=8219045888, available=6127353856, percent=25.4, used=1750753280, free=5216337920, active=1926008832, inactive=428765184, buffers=164847616, cached=1087107072, shared=29609984)

mem = psutil.virtual_memory()    #  获取内存完整信息
print mem.total                  # 获取内存总数
print mem.free                   # 获取空闲内存数

print psutil.swap_memory()     # 获取swap分区信息

# output
# sswap(total=8586784768, used=0, free=8586784768, percent=0.0, sin=0, sout=0)


# disk infomation

print psutil.disk_partitions()     # 获取磁盘完整信息

# output
# [sdiskpart(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro,data=ordered')]

print psutil.disk_usage('/')       # 获取分区使用情况

# output
# sdiskusage(total=23117426688, used=16678273024, free=5241262080, percent=76.1)

print psutil.disk_io_counters(perdisk = False)    # 获取单个分区IO个数　读写信息

# output
# sdiskio(read_count=56200, write_count=11285, read_bytes=1042426880, write_bytes=532283392, read_time=1175616, write_time=463460, read_merged_count=2322, write_merged_count=18428, busy_time=206464)


# network infomation

print psutil.net_io_counters()         # 获取网络总的io信息

# output
# snetio(bytes_sent=3901056, bytes_recv=49473060, packets_sent=34616, packets_recv=45911, errin=0, errout=0, dropin=0, dropout=0)

print psutil.net_io_counters(pernic = True)   # pernic = True 输出每个网络接口的ｉｏ信息


# output
# {'lo': snetio(bytes_sent=16273732, bytes_recv=16273732, packets_sent=8042, packets_recv=8042, errin=0, errout=0, dropin=0, dropout=0), 'ens33': snetio(bytes_sent=24070890, bytes_recv=58311178, packets_sent=53719, packets_recv=69150, errin=0, errout=0, dropin=0, dropout=0)}

print psutil.net_connections()


# other infomation

print psutil.users()          # 返回当前登录系统的用户信息

# output
# [suser(name='ubuntu', terminal='tty7', host='localhost', started=1498202752.0)]

print psutil.boot_time()     #获取开机时间

# output
# 1498202683.0

import datetime

print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')

# process infomation

print psutil.pids()        # 列出所有进程PID

p = psutil.Process(2751)

print p.name()         # 进程名
print p.status()       # 进程状态
print p.exe()          # 进程bin路径
print p.cwd()          # 进程工作目录绝对路径
print p.create_time()  # 进程创建时间，时间戳格式
print p.uids()         # 进程uid信息
print p.gids()         # 进程ｇｉｄ信息
print p.cpu_times()    # 进程CPU时间信息

# output
# pcputimes(user=0.22, system=0.33, children_user=12.49, children_system=1.44)

print p.cpu_affinity() # 进程CPU亲和度
print p.memory_percent()  # 进程内存利用率
print p.memory_info()     # 进程内存rss vms 信息

# output
# pmem(rss=12472320, vms=201814016, shared=6840320, text=11210752, lib=0, data=7532544, dirty=0)

print p.io_counters()     # 进程ｉｏ信息

# output
# pio(read_count=1789, write_count=359, read_bytes=6610944, write_bytes=57344, read_chars=4894923, write_chars=5140142)

print p.num_threads()      # 进程开启的线程数


# 获取用户启动的应用程序进程信息，跟踪进程的运行状态

from subprocess import PIPE

p = psutil.Popen(['/usr/bin/python', '-c', "print('hello')"], stdout = PIPE)

print p.name()

print p.username()

print p.cpu_times()
