# -*- coding: utf-8 -*-
# 常量模块

"""
将常量集中到一个文件，统一配置管理
"""


class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError, "Can't change const {0}".format(name)
        if not name.isupper():
            raise self.ConstCaseError, 'const name "{0}" is not all uppercase.'.format(name)
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()


import constant
constant.MAX_CONNECTION_TIME = 60
constant.MIN_BUFFER_SIZE = 300
