# 面向对象--装饰器--类实现
class check:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('登录验证')
        self.func()


# @check
def test():
    print('发说说')


test = check(test)
test()
