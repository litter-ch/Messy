# 面向对象-比较操作-上下文布尔值
class Person:

    def __init__(self, age):
        self.age = age

    # 满足条件返回再判断, 不满足直接为假
    def __bool__(self):
        return self.age >= 18


p1 = Person(20)
p2 = Person(10)
if p1:
    print('True')
else:
    print('False')


if p2:
    print('True')
else:
    print('False')