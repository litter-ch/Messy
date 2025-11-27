# 1.定义一个类
class Person:
    pass


# 2.根据这个类, 创建(实例化)一个对象
p = Person()

# 3.给p对象增加属性
p.age = 18
p.height = 180

# 4.查看属性
print(p.age)
# 以字典类型查看所有属性
print(p.__dict__)

p.pets = ['小花', '小黑']
print(f'{p.pets=}{id(p.pets)=}')

p.pets.append('小红')
print(f'{p.pets=}{id(p.pets)=}')

p.pets = ['小黄']
print(f'{p.pets=}{id(p.pets)=}')

# 删除属性
del p.pets
print(p.pets)
