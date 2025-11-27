class Money:
    pass


# 类也是对象
# 对象的方式增加属性
Money.count = 1
print(Money.__dict__)


# 类的方式增加属性
class Money:
    age = 18
    count = 1
    num = 666


print(Money.__dict__)
a = Money()
# 通过对象连接类 给类增加属性
a.__class__.sex = '男'
b = Money()
print(Money.__dict__)
print(b.sex)
