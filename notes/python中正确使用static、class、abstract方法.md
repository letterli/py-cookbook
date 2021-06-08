### Python中正确使用static、class、abstract方法

---

#### 实例方法

实例方法的定义只需要把第一个参数指定为self,该参数就是该类的一个实例对象。

```python
class Pizza(object):

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


Pizza.get_size()  // TypeError

Pizza.get_size(Pizza(42))  // 42

```

#### 静态方法

静态方法是一类特殊的方法。静态方法不依赖于对象本身的状态。
Python对象实例初始化一个绑定方法，绑定方法同样是对象，创建需要成本，静态方法就可以避免。

```python
class Pizza(object):

    def __init__(self, cheese, vegetables):
        self.cheese = cheese
        self.vegetables = vegetables

    @staticmethod
    def mix(x, y):
        return x + y

    def cook(self):
        return self.mix(self.cheese, self.vegetables)

Pizza().cook is Pizza().cook   # False

Pizza.mix is Pizza().mix    #  True

Pizza().mix is Pizza().mix   # True

```

#### 类方法

类方法不是绑定到实例对象上，而是绑定在类对象的方法。

```python
class Pizza(object):
    radius = 42

    @classmethod
    def get_radius(cls):
        return cls.radius

Pizza.get_radius is Pizza().get_radius  # True

Pizza.get_radius()     # 42

```

类方法通常使用场景：

##### 工厂方法

```python
class Pizza(object):

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())

```

##### 调用静态方法

```python
class Pizza(object):

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    @staticmethod
    def compute_area(radius):
        return math.pi * (radius ** 2)

    @classmethod
    def compute_volume(cls, height, radius):
        return height * cls.compute_area(radius)

    def get_volume(self):
        return self.compute_volume(self.height, self.radius)

```
