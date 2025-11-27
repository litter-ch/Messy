class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self}吃饭')

    def sleep(self):
        print(f'{self}睡觉')


class student(Person):
    def __init__(self, name, id, age=18):
        super().__init__(name, age)
        if isinstance(id, int):
            self.id = id

    def __str__(self):
        return f'年龄{self.age}学号{self.id}学生{self.name}在'

    def study(self):
        print(f'{self}学习')


class team_leader(Person):
    def __init__(self, name, id, age=18):
        super().__init__(name, age)
        if isinstance(id, int):
            self.id = id

    def __str__(self):
        return f'年龄{self.age}学号{self.id}组长{self.name}在'

    def study(self):
        print(f'{self}学习')

    def work(self):
        print(f'{self}管理学生')


class teacher(Person):
    def __init__(self, name, subject, age):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f'年龄{self.age}职务{self.subject}{self.name}老师在'

    def study(self):
        print(f'{self}教学')

    def work(self):
        print(f'{self}管理学生')


