# super(参数1,参数2) 参数2来判断传参方法  如参数2是实例对象就传的实例对象
# 参数1: 找谁的下一个节点  参数2: 用谁对应的类的MRO顺序查找
# python3版本直接super()就可以了
class C:
    age = 'C'

    def __init__(self):
        self.c = 'c'
        print(3)


class B(C):
    age = 'B'

    def __init__(self):
        self.b = 'b'
        print(2)

    @classmethod
    def class_B(cls):
        print('class_B')


class A(B):
    age = 'A'

    def __init__(self):
        # self是A类则通过A的MRO顺序 找B的下一个C类, 传self参数实例方法
        super(B, self).__init__()
        # python3版本()里面不写自动识别当前类的下一个类和当前方法的参数
        # 当前为A类 是self实例化参数方法
        super().__init__()
        self.a = 'a'
        print(1)

    @classmethod
    def class_A(cls):
        # 找A的下一个B类, 传A是类方法
        super(A, cls).class_B()
        print('class_A')


a = A()
print(a.c)
a.class_A()
