### 异常处理的三个好习惯

---

#### 只做最精确的异常捕获

异常处理工作由“捕获”和“抛出”两部分组成。
“捕获”指的是使用try...except包裹特定语句，妥当的完成错误流程处理；raise主动抛出异常。

```python
#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
import re

def save_website_title(url, filename):
    """获取某个地址的网页标题，然后将其写入到文件中

    :returns: 如果成功保存，返回True，否则打印错误，返回False
    """

    try:
        resp = requests.get(url)
        obj = re.search(r'<title>(.*)</title>', resp.text)
        if not obj:
            print 'Save failed: title tag not found in page content.'
            return False

        title = obj.group(1)
        with open(filename, 'w') as fp:
            fp.write(title)
            return True
    except Exception:
        print 'save failed: unable to save title of {url} to {filename}'
        return False


def main():
    save_website_title('https://www.qq.com', 'qq_title.txt')


if __name__ == '__main__':
    main()

```

脚本里save_website_title函数做了好几件事。首先通过网络获取网页内容，然后利用正则匹配标出标题，最后将标题
写在本地文件。有两个步骤容易出错：网络请求和本地文件操作。

异常捕获的目的，不是去捕获尽可能多的异常。只做最精确的异常捕获，就不会出现过于庞大、含糊的异常捕获。

精确捕获包括：
> * 永远只捕获那些可能会抛出异常的语句块
> * 尽量只捕获精确的异常类型，而不是模糊的Exception

```python
from requests.exceptions import RequestException


def save_website_title(url, filename):
    try:
        resp = requests.get(url)
    except RequestException as e:
        print 'Save failed: unable to get page content: {e}'
        return False

    # 这段正则操作本身就是不应该抛出异常的，所以我们没必要使用try语句块
    obj = re.search(r'<title>(.*)</title>')
    if not obj:
        print 'Save failed: title tag not found in page content'
        return False

    title = obj.group(1)

    try:
        with open(filename, 'w') as fp:
            fp.write(title)
    except IOError as e:
        print 'Save failed: unable to write to file {filename}: {e}'
        return False
    else:
        return True

```

#### 别让异常破坏抽象一致性

```python
# 在某个处理图像的模块内部
# <PROJECT_ROOT>/util/image/processor.py
def process_image(*args):
    try:
        image = Image.open(fp)
    except Exception:
        # 该异常将会被Django中间件捕获，返回错误信息
        raise error_codes.INVALID_IMAGE_UPLOADED

```

> * 让模块只抛出与当前抽象层级一致的异常,image.processor模块应该抛出自己封装的ImageOpenError异常
> * 在必要的地方进行异常包装与转换,在贴近高层抽象地方，将图像处理模块的ImageOpenError低级异常包装转换为高级异常

```python
# <PROJECT_ROOT>/util/image/processor.py
class ImageOpenError(Exception):
    pass

def process_image(*args):
    try:
        image = Image.open(fp)
    except Exception as e:
        raise ImageOpenError

# <PROJECT_ROOT>/app/views.py
def view_function(request):
    try:
        process_image(fp)
    except ImageOpenError:
        raise error_codes.INVALID_IMAGE_UPLOADED

```

requests模块请求页面出错时抛出的异常，并不是它在底层所使用的urllib3模块的原始异常，而是通过requests.exceptions包装的异常。

```python
try:
    requests.get('https://www.invalid-host-foo.com')
except Exception as e:
    print type(e)

# output: <class 'requests.exceptions.ConnectionError'>
```

urllib3模块是requests模块依赖的底层实现细节，这个细节有可能在未来版本发生变动。所以必须对它抛出的异常进行恰当的包装，
避免未来的底层变更对requests用户端错误处理逻辑产生影响。


#### 异常处理不应该喧宾夺主

异常处理逻辑过多，以至于扰乱了代码核心逻辑。代码里充斥着大量的try、except、raise语句，让核心逻辑变得难以辨识。

```python
def upload_avatar(request):
    """用户上传头像"""

    try:
        avatar_file = request.FILES['avatar']
    except KeyError:
        raise error_codes.AVATAR_FILE_NOT_PROVIDED

    try:
        resized_avatar_file = resize_avatar(avatar_file)
    except FileTooLargeError as e:
        raise error_codes.AVATAR_FILE_TOO_LARGE
    except ResizeAvatarError as e:
        raise error_codes.AVATAR_FILE_INVALID

    try:
        request.user.avatar = resized_avatar_file
        request.user.save()
    except Exception:
        raise error_codes.INTERNAL_SERVER_ERROR

    return HttpResponse({})

```

以上视图函数针对每件事都做了异常捕获。如果做某件事发生异常，就返回错误。
这样的处理流程纵然合理，但是显然代码里的异常处理逻辑有点“喧宾夺主”，很难提炼代码核心逻辑。

上下文管理器是一种配合with语句使用的特殊Python对象，通过它，可以让异常处理工作变得更方便。

```python
class raise_api_error(object):
    """captures specified exception and raise ApiErrorCode instead

    :raises: AttributeError if code_name is not valid
    """

    def __init__(self, captures, code_name):
        self.captures = captures
        self.code = getattr(error_codes, code_name)

    def __enter__(self):
        # 方法将在进入上下文时调用
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 方法将在退出上下文时调用
        # exc_type, exc_val, exc_tb 分别表示该上下文内抛出的异常类型、异常值、错误栈
        if exc_type is None:
            return False

        if exc_type == self.captures:
            raise self.code

        return False

```

定义raise_api_error上下文管理器，它在进入上下文时什么也不做。但在退出上下文时，会判断当前上下文中是否抛出了类型为
self.captures的异常，如果有，就用ApiErrorCode异常替代它。

```python
def upload_avatar(request):
    """用户上传新头像"""

    with raise_api_error(KeyError, 'AVATAR_FILE_NOT_PROVIDED'):
        avatar_file = request.FILES['avatar']

    with raise_api_error(ResizeAvatarError, 'AVATAR_FILE_INVALID'),\
            raise_api_error(FileTooLargeError, 'AVATAR_FILE_TOO_LARGE'):
        resized_avatar_file = resize_avatar(avatar_file)

    with raise_api_error(Exception, 'INTERNAL_SERVER_ERROR'):
        request.user.avatar = resized_avatar_file
        request.user.save()

    return HttpResponse()

```
