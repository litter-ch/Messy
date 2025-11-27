# 面向对象-生命周期
class Person:
    def __init__(self):
        print('初始化方法')

    # 对象被系统回收的时候触发
    def __del__(self):
        print('该对象被释放了')

    # 修改对象的创建过程
    def __new__(cls):
        # 在创建过程中执行
        print('新建了一个对象,被拦截了')


p = Person()
print(p)
