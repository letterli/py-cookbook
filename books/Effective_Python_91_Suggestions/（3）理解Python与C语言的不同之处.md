### 理解Python与C语言的不同之处

---

Python底层是用C语言实现的，但切忌使用C语言的思维和风格来编写Python.

##### “缩进” 与 "{}"

C、C++、Java语言使用花括号{}来分隔代码段不同，Python中使用严格的代码缩进方式分隔代码块。
严格的缩进确实能让代码更加规范、整齐，可读性和可维护性更高。
避免缩进带来的困扰的方法之一就是养成良好的习惯，统计缩进风格。

##### '' 与 ""

C语言中单引号(')与双引号(")有严格的区别，单引号代表一个字符，对应编译器字符集中一个整数值。
双引号则表示字符串，默认以'\0'结尾。

Python中，单引号与双引号没有明显区别，仅仅在输入字符串内容不同时，存在微小差异。

```python
# 字符串中本身的双引号需要转义
string1 = "He said, \"Hello.\""
# 字符串本身的双引号不需要转义
string2 = 'He said, "Hello."'
```

##### 三元操作符“ ? : ”

三元操作符是if...else的简写方法，语法形式为 C ? X : Y,它表示条件C为True的时候取值X，C为False的时候取值Y。

Python中 C ? X : Y 等价形式为 X if C else Y。

##### switch...case

Python中没有像C语言那样的switch....case分支语句。

```c
switch(n) {
    case 0:
        printf("You typed zero.\n");
        break;
    case 1:
        printf("You are in top\n");
        break;
    default:
        printf("Only single-digit numbers are allowed.\n");
        break;
}
```

```python
if n == 0:
    print "You typed zero.\n"
elif n == 1:
    print "You are in top\n"
else:
    print "Only single-digit numbers are allowed.\n"

def f(n):
    return {
        0: "You typed zero.\n",
        1: "You are in top\n"
    }.get(n, "Only single-digit numbers are allowed.\n")
```
