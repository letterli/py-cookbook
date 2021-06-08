#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
如何设计一个代码统计工具
用于统计项目中的代码行数，包括文件个数，代码行数，注释行数，空行行数

python code_counter --type python
"""

import os

def parse_sigle_py(path):
    """ 只能统计单行注释的py文件 """
    comments = blanks = codes = 0

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                blanks += 1
            elif line.startswith("#"):
                comments += 1
            else:
                codes += 1

    return {"comments": comments, "blanks": blanks, "codes": codes}

def parse_multi_comment_py(path):
    """ 可以统计包含多行注释的py文件 """
    in_multi_comment = False
    comments = blanks = codes = 0

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()

            # 多行注释中的空行当做注释处理
            if line == "" and not in_multi_comment:
                blanks += 1

            # 注释有四种
            # 1. #井号开头的单行注释
            # 2. 多行注释符在同一行的情况
            # 3. 多行注释符之间的行
            elif line.startswith("#") or (line.startswith('"""') and line.endswith('"""') and len(line) > 3) or \
                     (line.startswith("'''") and line.endswith("'''") and len(line) > 3) or (in_multi_comment and
                      not (line.startswith('"""') or line.startswith("'''"))):
                comments += 1
            # 4. 多行注释符的开始行和结束行
            elif line.startswith('"""') or line.startswith("'''"):
                in_multi_comment = not in_multi_comment
                comments += 1
            else:
                codes += 1

    return {"comments": comments, "blanks": blanks, "codes": codes}

def parse(path, exstansion="py"):
    CONF = {
        "py": {
            "start_comment": ['"""', "'''"],
            "end_comment": ['"""', "'''"],
            "single": "#"
        },
        "java": {
            "start_comment": ["/*"],
            "end_comment": ["*/"],
            "single": "//"
        }
    }

    start_comment = CONF.get(exstansion).get("start_comment")
    end_comment = CONF.get(exstansion).get("end_comment")
    in_multi_comment = False
    comments = blanks = codes = 0

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()

            cond2 = cond3 = cond4 = False

            for index, item in enumerate(start_comment):
                cond2 = line.startswith(item) and line.endswith(end_comment[index]) and len(line) > len(item)
                if cond2:
                    break

            for item in end_comment:
                if line.startswith(item):
                    cond3 = True
                    break

            for item in start_comment + end_comment:
                if line.startswith(item):
                    cond4 = True
                    break

            if line == "" and not in_multi_comment:
                blanks += 1
            elif line.startswith(CONF.get(exstansion).get("single")) or cond2 or \
                    (in_multi_comment and not cond3):
                comments += 1
            elif cond4:
                in_multi_comment = not in_multi_comment
                comments += 1
            else:
                codes += 1

    return {"comments": comments, "blanks": blanks, "codes": codes}

def counter(path):
    """
    统计目录或者某个文件
    """
    if os.path.isdir(path):
        comments = blanks = codes = 0
        list_dirs = os.walk(path)
        for root, dirs, files in list_dirs:
            for f in files:
                file_path = os.path.join(root, f)
                stats = parse(file_path)
                comments += stats.get("comments")
                blanks += stats.get("blanks")
                codes += stats.get("codes")
        return {"comments": comments, "blanks": blanks, "codes": codes}
    else:
        return parse(path)


if __name__ == '__main__':
    print parse("counter.py")
