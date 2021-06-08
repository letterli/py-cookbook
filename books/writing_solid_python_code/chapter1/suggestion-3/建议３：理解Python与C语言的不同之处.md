### 理解Python与C语言的不同之处

---

1) "缩进" 与 "{}"

与C、C++、Java语言使用花括号{}来分隔代码不同，Python使用严格的代码缩进方式分隔代码块。

2) ' 与 "

Python中，单引号与双引号没有明显区别，仅仅在输入字符串内容不同时，存在微小差异。

```python
first_string = "He said, \"Hello\""

second_string = 'He said, "Hello"'
```

3) 三元操作符 "?:"

C语言中三元操作符：　C ? X : Y C为True的时候取值X，C为False的时候取值Y。
Python中等价形式为： X if C else Y


4) switch...case

Python中没有像C语言的switch...case分支语句。

```c
switch(n) {
    case 0:
        printf("You typed zero.\n");
        break;
    case 1:
        printf("You are in top.\n");
        break;
    case 2:
        printf("n is an even number.\n");
        break;
    default:
        printf("Only single-digit numbers are allowed.\n");
        break;
}
```
```python
if n == 0:
    print("You typed zero.\n")
elif n == 1:
    pass
elif n == 2:
    pass
else:
    pass
```

