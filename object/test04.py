class Money:
    age = 18
    count = 1
    num = 666


a = Money()
print(f'{a.age=}')

# 类的方式改属性
Money.age = 19
print(f'{a.age=}')

# 通过对象连接类 改类的属性
a.__class__.age = 19
a.age = 20
print(f'{a.age=}')
print(a.__class__.age)
b = Money()
print(f'{b.age=}')
