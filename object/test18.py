# 只读属性
class Person:
    # 实现伪私有属性外界不可写
    def __init__(self):
        self.__age = 18

    @property  # 可以把使用属性的方式来使用这个方法
    def age(self):
        return self.__age
        # 实现外界可读

    #  可以在上面的基础上实现可写
    # @age.setter
    # def age(self, value):
    #     self.__age = value


p1 = Person()
print(p1.age)

try:
    p1.age = 20
    print(p1.age)
except Exception:
    print('只可读,不可修改')

# 伪私有 可以通过底层代码修改
p1._Person__age = 20
print(p1.age)
p1.__dict__['_Person__age'] = 21
print(p1.age)