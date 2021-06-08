#### argparse

---

argparse 命令行和参数解析工具。

命令行与参数解析就是当你输入cmd 打开dos 交互界面时候，启动程序要进行的参数给定。

```shell
python pythonfile.py -f filename -n 10

```

##### python命令行参数解析步骤

> * 创建解析
> * 添加参数
> * 解析参数

##### 添加参数过程参数设定

```python
# ArgumentParser.add_argument(name or flags...[, action][, nargs][, const]
                              [, default][, type][, choices][, required]
                              [, help][, metavar][, dest])

```

###### name or flags

optional arguments以'-'为前缀的参数

###### action

命令行参数的操作，操作的形式有以下几种：
> * store:仅仅存储参数的值（默认）
> * storeconst:存储const关键字指定的值

```python
parser.add_argument('-t', action='store_const', const=7)
```

> * store_true/store_false:值为True/False

```python
parser.add_argument('-t', action='store_true')
```

###### count

统计参数出现的次数

```python
parser.add_argument('--count', '-c', action='count')
parser.parse_args('-cccc'.split())
```

###### help

显示help信息

###### version

```python
parser.add_argument('--version', action='version', version='version 2.0')
parser.parse_args('--version')
```

###### nargs

1. N: N个参数
2. ?: 首先从命令行获取参数，若没有则从const获取，仍然没有则从default获取
3. */+　任意多个参数

###### default

默认值

###### const

保存为常量

###### choices

设置参数范围

```python
parser.add_argument('number', type=int, choices=range(1, 4))
```

###### type

参数类型

###### dest

参数别名

###### required

是否为必选参数，默认为True

###### metavar

帮助信息中显示的参数名称



