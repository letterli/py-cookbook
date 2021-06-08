#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def sum_args():
    parser = argparse.ArgumentParser(usage='python argparse_dev.py [-h] [-s] N [N ...]',
                                     description='sum the integers',
                                     epilog='-'*50)
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers')
    args = parser.parse_args()
    print(args.accumulate(args.integers))


def person_info():
    parser = argparse.ArgumentParser(description='Personal Infomation')
    parser.add_argument('name', type=str, help='Your name')
    parser.add_argument('birth', type=str, help='Your birthday')
    parser.add_argument('-r', '--race', type=str, dest='race', help='Your race')
    parser.add_argument('-a', '--age', type=int, dest='age', default=0,
                        choices=range(150), help='Your age')
    parser.add_argument('-s', '--sex', type=str, dest='sex', default='male',
                        choices=['male', 'female'], help='Your sex')
    parser.add_argument('-g', '--girl', type=str, dest='girl', default='None',
                        nargs='*', help='Your girlfriend')
    parser.add_argument('-o', '--other', type=str, dest='other', required=False,
                        nargs='*', help='Othe Infomation')
    args = parser.parse_args()

    print('argparse.args = {0}'.format(args), type(args))
    print('name = {0}'.format(args.name))

    d = args.__dict__
    for key, value in d.items():
        print('{0} = {1}'.format(key, value))


def parse_argument():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--count', '-c', action='count')
    parser.add_argument('--version', action='version', version='version 2.0')
    parser.parse_args()


def main():
    parse_argument()


if __name__ == '__main__':
    main()
