# 元类: type  相当于于对象的祖先 最初的类
num = 10
print(num.__class__) # num对象由int 类实例化出来的

a = 'abc'
print(a.__class__)  # a对象由str 类实例化出来的


class Person:
    pass


p = Person()
print(p.__class__)  # p对象由Person 类实例化出来的

print(int.__class__)  # int对象由type 类实例化出来的

print(type.__class__)  # type对象由type 类实例化出来的
