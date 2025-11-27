# 比较操作
# 类里没有找到定义的函数会调换参数  但并不会叠加
# p1 > p2  没有定义__gt__ 会调换参数p2 < p1 再找有没有定义__lt__
class Person:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    # 判断是否相等
    def __eq__(self, other):
        print('==')

    # 判断是否不相等
    def __ne__(self, other):
        print('!=')

    # 判断是否大于
    def __gt__(self, other):
        print('>')

    # 判断是否大于等于
    def __ge__(self, other):
        print('>=')

    # 判断是否小于
    def __lt__(self, other):
        print('<')

    # 判断是否小于等于
    def __le__(self, other):
        print('<=')


p1 = Person(20, 180)
p2 = Person(20, 175)


print(p1 >= p2)

