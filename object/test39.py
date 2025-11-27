class B:
    a = 1  # 类属性
    def __init__(self):  # 实例属性
        self.b = 2


class A(B):
    def __init__(self):
        self.a = 3
        print(123)


class C(B):
    pass


a_obj = A()
c_obj = C()
print(A.a)
print(c_obj.b)
try:
    print(a_obj.b)
except:
    print('A已经定义了__init__实例属性, 访问不到B定义的__init__')
    print('可以在__init__里面加 B.__init__(self) 自动调用')
    print('但是这样可能会产生重复调用并且B类名字一改, 加的也要一起改')
    print('这个问题可以通过super解决  test40.py')
print(a_obj.a)
