### 编写Pythonic代码

---

##### 避免劣化代码

1) 避免只用大小写来区分不同的对象。

2) 避免使用容易引起混淆的名称。
重复使用上下文变量名、误用内建名称、使用element、list、dict作为变量名、使用0/1混淆

```python
# bad
def funA(list, num):
    for element in list:
        if num == element: return True
        else: pass

# perfect
def find_num(searchList, num):
    for listValue in searchList:
        if num == listValue: return True
        else: pass

```

3) 不要使用过长的变量名

```python
person_info = {
    'name': 'letterli',
    'IDCard': 'cmcc',
    'address': 'guangdong'
}
```

##### 深入认识Python有助于编写Pythonic代码

1) 全面掌握Python提供特性，包括语言特性和库特性。

2) 学习Python新版本提供的特性
Python版本随时间推移不断更新，使用正确的惯用法编写代码。

3)深入学习业界公认的比较Pythonic的代码。Flask、gevent、requests

```shell
# 使用pep8检测Python编码风格遵循PEP8原则

pip install pep8

pep8 --show-source --show-pep8 python_script.py

# 检测项目的质量
pep8 --statistics -qq project_dir

```

