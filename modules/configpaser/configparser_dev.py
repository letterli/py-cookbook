#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version:  python 2.7
# author:  letterli

import ConfigParser


def db_config():
    config = ConfigParser.ConfigParser(allow_no_value=True)

    config.read('my.cnf')
    print(config.sections())

    mysqld_options = config.options('mysqld')
    print(mysqld_options)

    mysqld_items = config.items('mysqld')
    print(mysqld_items)

    mysqld_port = config.get('mysqld', 'port')
    mysqld_server_id = config.getint('mysqld', 'server-id')
    print(mysqld_port)
    print(mysqld_server_id)

    # change option value
    config.set('mysqld', 'max_connections', 250)
    config.write(open('my.cnf', 'w'))

    # add section
    config.add_section('debug')
    config.set('debug', 'level', 'info')
    config.set('debug', 'message', 'debug')
    config.write(open('my.cnf', 'w'))

    # remove section or option
    config.remove_option('debug', 'message')
    config.remove_section('debug')
    config.write(open('my.cnf', 'w'))


if __name__ == '__main__':
    db_raw_config()


