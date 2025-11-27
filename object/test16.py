class Animal:
    __age = 10

    def test(self):
        print(Animal.__age)
        print(self.__age)

    pass


class Dog(Animal):
    def test2(self):
        print(Dog.__age)
        print(self.__age)

    pass


# 由于私有化属性这两个访问不了
# print(Animal.__age)
# print(Dog._age)

# 命名重整机制 通过__dict__查询到 __age 被改为 _类名__age
print(Animal.__dict__)
print(Animal._Animal__age)
print(Dog._Animal__age)
