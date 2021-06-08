### 优雅的python

---

#### pythonic

优雅的、地道的、整洁的python代码

#### 链式比较

```python
a, b = 3, 1

# Pythonic
1 <= b <= a < 10

```

#### 变量交互

```python
a, b = b, a

```

#### 真值测试

| 真        | 假   |
| :--------:   | :-----:  |
| True                | False           |
| 任意非空字符串        |   空的字符串 ''   |
| 任意非零数字          |    数字 0        |
| 任意非空容器          |    空的容器 [] () {} set()    |
| 其他任意非False       |    None         |

```python
name = 'Tim'
langs = ['a', 'b', 'c']
info = {'name': 'Tim', 'sex': 'male', 'age': 18}

# Pythonic
if name and langs and info:
    pass

```

#### 字符串反转

```python
# Pythonic
def reverse_str(string):
    return string[::-1]

```

#### 字符串格式化

```python
str = "welcome to {blog} and following {wechat}".format(blog="xxx", wechat="xxx")

```

#### 字符串列表连接

```python
strList = ["Python", "is", "good"]

# Pythonic
res = ' '.join(strList)

```

#### 列表求和，最大值，最小值，乘积

```python
numList = [1, 2, 3, 4, 5]

# Pythonic
sum = sum(numList)
maxNum = max(numList)
minNum = min(numList)

from operator import mul
prod = reduce(mul, numList, 1)

```

#### 推导式

```python
# 列表推导式
[i for i in xrange(10)]

# 生成器表达式
g = (i for i in xrange(10))

# 字典推导式
numbers = [1, 2, 4]
{number: number * 2 for number in numbers if number > 1}

```

#### 字典的默认值

```python
dic = {'name': 'admin', 'age': 22}

dic['workage'] = dic.get('workage', 0) + 1

```

#### 预设字典默认值
通过key分组的时候，不得不每次检查key是否已经存在于字典中。

```python
# Non-Pythonic
data = [('foo', 10), ('bar', 20), ('foo', 39), ('bar', 49)]
groups = {}

for (key, value) in data:
    if key in groups:
        groups[key].append(value)
    else:
        groups[key] = value

# pythinic
groups = {}

for (key, value) in data:
    groups.setdefault(key, []).append(value)

from collections import defaultdict
groups = defaultdict(list)

for (key, value) in data:
    groups[key].append(value)

```

#### for...else...语句

```python
for x in xrange(1, 5):
    if x == 5:
        break
else:
    pass

```

#### 三元符

```python
a = 3

b = 2 if a > 2 else 1

dic = None
b = dic or {}

```

#### Enumerate

```python
array = [1, 2, 3, 4, 5]

for index, value in enumerate(array):
    print index, value

```

#### 循环遍历区间元素

```python
xrange返回生成器对象，生成器比列表更节省内存。python3 range方法和python2中xrange方法一样。

# python2
for i in xrange(n):
    pass

# python3
for i in range(n):
    pass

```

#### 使用zip创建键值对

```python
keys = ['name', 'sex', 'age']
values = ['admin', 'male', '18']

dic = dict(zip(keys, values))

```

#### 使用生成器 yield

```python
(x for x in range(10) if x % 2 == 0)

def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a + b

```

#### try...except...else...finally

```python
try:
    db.execute('UPDATE table SET age = 19 WHERE id = 1')
except DBError:
    db.roolback()
else:
    db.commit()
finally:
    pass

```

#### 用with子句自动管理资源

```python
with open('filename', 'r') as f:
    for line in f:
        pass

```

#### 善用装饰器
装饰器可以把与业务逻辑代码无关的代码抽离，让代码保持干净清爽，而且装饰器能重复利用。

```python
# Non-Pythonic
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# pythonic

import urllib
import urllib.request as urllib

def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page
    return wrapper

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

```

#### 合理使用列表

列表对象（list）是一个查询效率高于操作的数据结构，比如删除一个元素和插入一个元素时执行效率就非常低，因为还要对剩下的元素进行移动。
deque是一个双向队列的数据结构，删除元素和插入元素会很快。

```python
names = ['a', 'b', 'c', 'd', 'f']
names.pop(0)
names.insert(0, 'aa')

# pythonic
from collections import deque

names.popleft()
names.appendleft('aa')

```

#### 遍历字典的key和value

```python
# python2
for key, value in d.iteritems():
    pass

# python3
for key, value in d.items():
    pass

```

