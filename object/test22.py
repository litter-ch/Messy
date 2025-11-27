class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 将对象转换为字符串, 返回方法中的字符串内容, 用于给客户
    def __str__(self):
        return f'姓名:{self.name} 年龄:{self.age}'

    # 用于给开发人员, Python解释器看
    def __repr__(self):
        return 'xxx'


p1 = Person('Jack', 18)
print(p1.name, p1.age)

p2 = Person('Tom', 19)
print(p2.name, p2.age)

print(p1)
print(repr(p1))
