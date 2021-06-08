### lambda匿名函数

---

#### 简介

lambda函数又称匿名函数，匿名函数就是没有名字的函数。

```python
add = lambda x, y: x + y

# 等同于

def add(x, y):
    return x + y

```

#### 函数式编程

map、reduce、filter、sorted高阶函数支持函数作为参数，lambda函数可应用在函数式编程。

```python
lst = [3, 5, -4, -1, 0, -2, -6]

sorted(lst, key=lambda x: abs(x))

```

#### 闭包

```python
def add(n):
    return lambda x: x + n

```
