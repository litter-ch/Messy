class Person():
    def eat(self):
        print('这是一个实例方法', self)

    @classmethod
    def leifangfa(cls):
        print('这是一个类方法', cls)

    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')


p = Person()
print(p.__dict__)


# 万物皆对象, 函数也是一个对象
def run():
    print('run!')


# 将函数这个对象, 添加到p的属性里面
p.sport = run
print(p.__dict__)
