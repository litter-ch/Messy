import abc


# 设置成抽象类, 不能直接创建对象, 通过它的子类创建对象
class Animal(object, metaclass=abc.ABCMeta):
    # 抽象方法, 子类必须重新用到这个方法
    @abc.abstractmethod
    def speak(self):
        print(1)
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪')


class Cat(Animal):
    def speak(self):
        print('喵喵喵')


def test(obj):
    obj.speak()


d = Dog()
c = Cat()
test(d)
test(c)
