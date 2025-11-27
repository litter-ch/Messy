class Money:
    age = 20
    sex = 'female'

one = Money()

# one 对象本身没有age 属性
print(one.__dict__)

# 用到的是类的属性
print(one.age)
print(Money.__dict__)

# 直接在对象的属性字典里修改, 类的属性字典不可更改
one.__dict__ = {'height': 180, 'sex': 'female'}
print(one.sex)
print(one.__dict__)

one.__dict__ = {'name': 'Jack', 'sex': 'male'}
print(one.name)

print(Money.__dict__)
