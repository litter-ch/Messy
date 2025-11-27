# 格式: isinstance(object, class) 判断一个对象object 是否是后面这个class类型
class Person1:

    # __init__ 作用: 当我们创建好一个实例对象之后, 会自动调用这个方法, 来初始化对象
    def __init__(self):
        self.__age = 18  # 对私有属性保护

    # 内部访问私有属性
    def set_age(self, value):

        # 数据滤波
        if isinstance(value, int) and 0 < value < 200:
            self.__age = value
        else:
            print('数据输入有问题')

    # 获取私有属性的值
    def get_age(self):
        return self.__age


p1 = Person1()
p1.set_age(20)
print(p1.get_age())
