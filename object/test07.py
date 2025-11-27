# 限制对象属性的添加
class Person:
    __slots__ = ('name', 'age')


p = Person()
p.name = 'Jack'

# 没有限制类属性的添加
p.__class__.num = 1
print(p.num)
print(p.name)

o = Person()
print(o.num)

# 限制了对象属性的添加
try:
    p.sex = 'male'
    print(p.sex)
except Exception:
    print('限制了对象属性的添加, 属性添加失败')
