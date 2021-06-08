### 编写Pythonic代码

---

#### 要避免劣化代码

> 1.避免只用大小写来区分不同的对象。

```python
# a是一个数值类型变量，A是String类型
# 编码过程中很容易区分二者含义，但毫无益处，不方便阅读

a = 13
A = 'string'
```

> 2.避免使用容易混淆的名称。

```python
# 变量名与所要解决的问题域一致
# 示例一
def funA(list, num):
    for element in list:
        if num == element:
            return True
        else:
            return False

# 示例二
def find_num(searchList, num):
    for listValue in searchList:
        if num == listValue:
            return True
        else:
            return False

```

> 3.不要害怕过长的变量名。

```Python
# 为了使程序更容易理解和阅读，有时候长变量名是必须的。

person_info = {
    'name': 'Jon',
    'card_number': '20190316',
    'address': 'GD',
    'email': 'admin@gail.com'
}
```

#### 深入认识Python有助于编写Pythonic代码

> 1.全面掌握Python提供给我们的所有特性，包括语言特性和库特性。
> 2.随着Python的版本更新、时间推移，Python语言不断演进，学习每个Python新版本的特性，掌握它的变化趋势。
> 3.深入学习业界公认的比较Pythonic的代码，比如Flask、gevent、requests。

使用一个Pythonic程序库可以简化很多工作量。Python标准库urllib2，代码非常复杂。
而使用requests则优美简洁。

```python
import urllib2
gh_url = 'https://api.github.com'
req = urllib2.Request(gh_url)
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'passwd')
auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)
urllib2.install_opener(opener)
handler = urllib2.urlopen(req)
print handler.getcode()
print handler.headers.getheader('content-type')
```

```python
import requests
r = requests.get('https://api.github.com', auth=('user', 'passwd'))
print r.status_code
print r.headers['content-type']

```

PEP8 Python编码风格指南，保持代码一致性细节要求。

```python

if name == 'admin':
    do_sth_for_admin()

do_one_thing()
do_two_thind()

```
