### 理解Pythonic概念

---

##### Pythonic定义

充分体现Python自身特色的代码风格。

##### 代码风格

在语法上，代码风格要充分表现Python自身特色。

```python
# 变量交换
a, b = b, a

# 遍历列表
for i in alist:
    do_sth_with(i)

# 安全关闭文件描述符
with open(path, 'r') as f:
    do_sth_with(f)

# 更好地体现Pythonic
list(reversed(a))

```

##### 标准库

```python
# 字符串格式化

'{greet} from {language}.'.format(greet='Hello World', language='Python')

```

##### Pythonic的库或框架

```python
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World.'

if __name__ == "__main__":
    app.run()

```

> * 包和模块的命名采用小写、单数形式，而且短小。
> * 包通常仅作为命名空间，如只包含空的__init__.py文件。
