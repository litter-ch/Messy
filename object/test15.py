class Animal:
    __age = 10

    def test(self):
        print(Animal.__age)
        print(self.__age)

    pass


# Animal的子类
class Dog(Animal):
    def test2(self):
        print(Dog.__age)
        print(self.__age)

    pass


# print(Animal.__age)
# print(Dog._age)

a = Animal()
a.test()

# d = Dog()
# d.test2()
