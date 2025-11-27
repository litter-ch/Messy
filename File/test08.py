import contextlib


# 这个装饰器可以将生成器函数变成上下文管理器
@contextlib.contextmanager
def text():
    print(1)
    # yield上面的为enter
    yield 'xxx'  # yield后面的赋值给t
    # yield下面的为exit
    print(2)


with text() as t:
    print(3, t)
