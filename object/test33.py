# 面向对象-描述器2
# 一般通过实例去操作描述器2, 且只有在新式类中生效(继承自object)
# 资料描述器 实现了get set
# 非资料描述器 仅仅实现了get方法
# 描述器和实例属性同名时的调用优先级:  资料描述器 > 实例属性 > 非资料描述器
class Age:
    def __get__(self, instance, owner):
        print('1')

    def __set__(self, instance, value):
        print('2')

    def __delete__(self, instance):
        print('3')


class Person:
    age = Age()


p = Person()
p.age = 18
print(p.age)
del p.age
