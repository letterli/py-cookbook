### ConfigParser模块

---

#### 简介

ConfigParser模块在python3中修改为configparser。
模块的作用 就是使用模块中的RawConfigParser()、ConfigParser()、 SafeConfigParser()方法，
创建一个对象使用对象的方法对指定的配置文件做增删改查 操作。


#### 方法

```python
    import ConfigParser

    config = ConfigParser.ConfigParser()

    # 读取配置文件
    config.read(filename)         # 直接读取文件
    config.get(setion, option)    # 获取section下具体某一项的值
    config.setions()              # 得到所有section，并以列表形式返回
    config.options(section)       # 得到section下的所有option
    cofig.items(section)          # 键值对的形式得到section下的所有option
    config.getint(section, option)
    config.getfloat(section, option)
    config.getboolean(section, option)

    # 写入配置文件
    config.add_section(section)           # 添加一个新的section
    config.set(section, option, value)    # 对section添加option和value
    config.remove_section(section)        # 删除某个section
    config.remove_option(section, option) # 删除某个section下的option
    config.write(open(filename, 'w'))     # 将section option的改动写入文件

    # 配置文件中的空值

    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(filename)
    config.get('section', 'option')   # option 没有设置值
    config.set('section', 'option')   # 设置option没有值

```
