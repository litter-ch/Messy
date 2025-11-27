# 单继承
# 无重叠多继承
# 有重叠多继承
# MRO原则: Method Resolution Order 方法解析顺序
# 深度优先: 根节点压入栈中, 每次从栈中弹出一个元素, 搜索所有在它下一级的元素, 重复
# python2.2之前全是经典类没有新式类   深度优先, 违背'重写可用原则'
# python2.2之后存在新式类   可以导入inspect模块
# python2.2版本的新式类(经典类不变)在2.2版本的'深度优先'基础上优化, 如果产生重复元素, 会保留最后一个
# python2.3版本-python2.7版本  新式类使用C3算法(经典类不变)
# python3版本之后没有经典类, 全是新式类 C3算法
# 广度优先: 根节点放到队列的末尾, 每次从队列的头部取出一个元素, 将这个元素所有的下一级元素放到队列的末尾, 重复


# 类.__mro__也可以获得mro顺序
# 类.mro() 也可以
import inspect
# inspect.getmro(类) 检查类的继承往上的顺序


class C:
    age = 'c'
    pass


class B(C):
    age = 'b'
    pass


class A(B):
    age = 'a'
    pass


print(inspect.getmro(A))

print(A.__mro__)
