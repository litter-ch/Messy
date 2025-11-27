class Person:
    age = 10


p = Person()


# 访问属性, 没有就去类里面继续访问
print(p.age)

# 赋值, 对象有这个属性就是修改, 没有就是新增这个属性
p.age += 5

# 访问属性
print(Person.age)
print(p.age)