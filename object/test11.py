# 不同类型的方法中访问不同类型属性的权限问题
class Person:
    age = 10

    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.num)

    @classmethod
    def leifangfa(cls):
        print(cls)

    @staticmethod
    def jingtaifangfa():
        print(Person.age)


p = Person()
p.num = 10

p.shilifangfa()

p.jingtaifangfa()