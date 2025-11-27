# __class__  查看属于哪一个类型实例化创建
# __bases__  查看属于由哪个父类继承的子类
# property在新式类中的使用
class Person(object):
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    age = property(get_age, set_age)


print(Person.__bases__)

p = Person()
print(p.age)
p.age = 20
print(p.age)
