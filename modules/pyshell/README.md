### Python调用shell命令

---

#### 通过os模块

system方法会创建子进程运行外部程序,方法只返回外部程序的运行结果.

example

```python
    import os

    output = os.system('shell command')   # output 状态码, 命令直接打印结果
```

popen方法不仅仅返回结果，还返回一个类文件对象,通过调用对象的read()或readlines()读取内容.

example

```python
    import os

    f = os.popen('shell command')   # 返回类文件对象
    output = f.readlines()
```

#### 通过commands模块

使用commands模块的getoutput()或getstatusoutput()方法，将外部程序的输出结果当做字符串返回.

example

```python
    import commands

    status, output = commands.getstatusoutput('shell command')
    output = commands.getoutput('shell command')
```

#### 通过subprocess模块

subprocess模块可以创建新的进程，可以与新建进程的输入/输出/错误管道连接，并可以获得新建进程的执行返回状态。

使用subprocess目的是替代os.system()、os.popen()、commands.getstatusoutput()

example

```python
    import subprocess

    # 如果command不是一个可执行文件，shell=True是不可省略的。
    # shell=True意思是shell下执行command

    subprocess.call('shell command', shell=True)  # 直接打印结果
    subprocess.Popen('shell command', shell=True) # 直接打印结果
    p1 = subprocess.Popen('shell command', stdout=subprocess.PIPE, shell=True)
    p1.communicate()   # 返回一个tuple, (标准输出和错误)

```
