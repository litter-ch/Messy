# 面向对象-描述器1
class Person:
    def __init__(self):
        self.__age = 10

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def del_age(self):
        del self.__age
    # age描述器 实现了修改获取删除方法
    age = property(get_age, set_age, del_age)


p = Person()
p.age = 10
print(p.age)

help(Person)