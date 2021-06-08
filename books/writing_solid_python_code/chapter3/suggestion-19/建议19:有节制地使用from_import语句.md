### 有节制地使用from...import语句

---

Python提供了三种方式来引入外部模块：import语句、from...import...以及__import__函数。

使用import注意事项：
> * 一般情况下尽量优先使用import a形式，如访问B时需要使用a.B的形式。
> * 有节制地使用from a import B形式，可以直接访问B。
> * 尽量避免使用from a import *形式，会污染命名空间，无法清晰表示导入对象。

Python在初始化运行环境时会预先加载一批内建模块到内存中，这些模块相关的信息被存放在sys.modules中。

加载一个模块时，解析器实际上完成了以下动作：
> *
