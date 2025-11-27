import abc


class Animal(metaclass=abc.ABCMeta):
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self}吃饭')

    def play(self):
        print(f'{self}玩')

    def work(self):
        pass

    def sleep(self):
        print(f'{self}睡觉')


class Dog(Animal):
    def work(self):
        print(f'{self}看家')

    def __str__(self):
        return f'名字{self.name}年龄{self.age}的小狗在'


d = Dog('小黑', 7)


class Cat(Animal):
    def __str__(self):
        return f'名字{self.name}年龄{self.age}的小猫在'

    def work(self):
        print(f'{self}抓老鼠')


c = Cat('小黄', 4)
c.eat()
c.work()


class Person(Animal):
    def __init__(self, name, pets, age=1):
        super().__init__(name, age)
        self.pets = pets

    def __str__(self):
        return f'名字{self.name}年龄{self.age}的人在'

    def keep_a_pet(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def work(self):
        for pet in self.pets:
            pet.work()


p = Person('Jack', [c, d], 4)
# p.keep_a_pet()
# p.work()