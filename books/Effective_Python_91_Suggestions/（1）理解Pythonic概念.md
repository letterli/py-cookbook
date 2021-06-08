### 建议1：理解Pythonic概念

---

#### 《The Zen of Python》

Beautiful is better than ugly.                                           优美胜于丑陋。
Explicit is better than implicit.                                        显式胜于隐式。
Simple is better than complex.                                           简单胜于复杂。
Complex is better than complicated.                                      复杂胜于难懂。
Flat is better than nested.                                              扁平胜于嵌套。
Sparse is better than dense.                                             稀疏胜于紧密。
Readability counts.                                                      可读性应当被重视。
Special cases aren't special enough to break the rules.                  尽管实用性会打败纯粹性，特例也不能凌驾于规则之上。
Although practicality beats purity.
Errors should never pass silently.                                       不要忽视任何错误，除非你确认要这么做。
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.                面对不明确定义，拒绝猜测的诱惑。
There should be one-- and preferably only one --obvious way to do it.    找到一种最好唯一的方法解决问题。
Although that way may not be obvious at first unless you're Dutch.       虽然一开始这种方法不是显而易见，因为你不是Python之父。
Now is better than never.                                                做好过不做，但没有思考的做还不如不做。
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.               如果实现很难说明，那它是个坏想法。
If the implementation is easy to explain, it may be a good idea.         如果实现容易解释，那它可能是个好想法。
Namespaces are one honking great idea -- let's do more of those!         命名空间是个绝妙的想法，请多加利用。


#### Pythonic定义

遵循Pythonic的代码，看起来就像伪代码。

```python
# 伪代码
function quicksort('array')
    if length('array') <= 1
        return 'array'
    select and remove a pivot element 'pivot' from 'array'
    create empty lists 'less' and 'greater'
    for each 'x' in 'array'
        if 'x' <= 'pivot' then append 'x' to 'less'
        else append 'x' to 'greater'
    return concatenate(quicksort(less), list('pivot'), quicksort('greater'))

# python 实现快速排序

def quicksort(array):
    less = []; greater = [];
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)

```

#### 代码风格

```python
# 变量交换
a, b = b, a

# 遍历容器
for i in aList:
    do_sth_with(i)

# 安全关闭文件描述符
with open(path, 'r') as f:
    do_sth_with(f)

aList = [1, 2, 3, 4]
list(reversed(aList))

```

#### 标准库

```python
# 字符串
value = {'great': 'Hello World.', 'language': 'Python'}
'%{great}s from %(language)s.' % value

# Pythonic
'{great} from {language}.'.format(great='Hello World.', language = 'Python')
```

#### Pythonic的库和框架

Flask框架业内认可的比较Pythonic的框架。

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hell():
    return 'Hello world.'

if __name__ == '__main__':
    app.run()

```

> ** 包和模块的命名采用小写、单数形式，而且短小。 **
> ** 包通常仅作为命名空间，如只包含空的__init__.py **
