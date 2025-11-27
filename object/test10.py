class Person:
    def eat(self, food):
        print('在吃饭,', food)

    @classmethod
    def leifangfa(cls, a):
        print('这是一个类方法', a)

    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')
p = Person()

# 解释器自动把p这个实例化对象传进去了
p.eat('potato')

# 类调用类方法
Person.leifangfa(123)
# 通过对象调用类方法, 装饰器让传递的第一个参数为类
p.leifangfa(123)
# 对象调用静态方法
p.jingtaifangfa()