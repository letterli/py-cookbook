#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
datetime 模块提供用于处理日期和时间的类。

##### 时间格式

| 格式符   | 说明     |
| :----:  | :----:  |
|%a  |星期的英文单词的缩写：如星期一， 则返回 Mon|
|%A  |星期的英文单词的全拼：如星期一，返回 Monday|
|%b  |月份的英文单词的缩写：如一月， 则返回 Jan|
|%B  |月份的引文单词的缩写：如一月， 则返回 January|
|%c  |返回datetime的字符串表示，如03/08/15 23:01:26|
|%d  |返回的是当前时间是当前月的第几天|
|%f  |微秒的表示： 范围: [0,999999]|
|%H  |以24小时制表示当前小时|
|%I  |以12小时制表示当前小时|
|%j  |返回 当天是当年的第几天 范围[001,366]|
|%m  |返回月份 范围[0,12]|
|%M  |返回分钟数 范围 [0,59]|
|%P  |返回是上午还是下午–AM or PM|
|%S  |返回秒数 范围 [0,61]。。。手册说明的|
|%U  |返回当周是当年的第几周 以周日为第一天|
|%W  |返回当周是当年的第几周 以周一为第一天|
|%w  |当天在当周的天数，范围为[0, 6]，6表示星期天|
|%x  |日期的字符串表示 ：03/08/15|
|%X  |时间的字符串表示 ：23:22:08|
|%y  |两个数字表示的年份 15|
|%Y  |四个数字表示的年份 2015|
|%z  |与utc时间的间隔 （如果是本地时间，返回空字符串）|
|%Z  |时区名称（如果是本地时间，返回空字符串）|
"""

import time
import datetime


def format_datetime():
    """datetime格式化时间"""
    dt = datetime.datetime.now()
    dt.strftime('%Y-%m-%d %H:%M:%S')     # 2020-07-28 09:58:16
    dt.strftime('%Y-%m-%d %H:%M:%S %p')  # 20-07-28 09:58:16 AM
    dt.strftime('%a')  # Tue
    dt.strftime('%A')  # Tuesday
    dt.strftime('%b')  # Jul
    dt.strftime('%B')  # July
    dt.strftime('%c')  # Tue Jul 28 09:58:16 2020
    dt.strftime('%w')  # 2   (这周的第2天)
    dt.strftime('%j')  # 210 (今年的第210天)
    dt.strftime('%U')  # 30 (今年的第30周)
    dt.strftime('%d')  # 28 (当月的第28天)


def string_to_datetime():
    """string转换成datetime"""
    dt_str = '2020-07-28'
    dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d')


def datetime_to_timestamp():
    """datetime转换为时间戳"""
    timestamp = time.mktime(dt.timetuple())


def timestamp_to_string():
    """时间戳转换成时间字符串"""
    sdt = time.strftime('%Y-%m-%d', time.localtime(timestamp))
    dt = datetime.datetime.fromtimestamp(timestamp)
    sdt = dt.strftime(dt, '%Y-%m-%d')


