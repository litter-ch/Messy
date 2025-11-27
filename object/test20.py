# 解决了test18 通过底层代码._Person__age改伪私有
class Person:
    # 当对象.属性 = 值 时, 会自动调用这个方法
    # 只有在方法内部才能真正的存储到__dict__字典里面
    def __setattr__(self, key, value):
        print(key, value)
        # 1 判定key 是否是只读属性的名称
        if key == 'age' and 'age' in self.__dict__:
            print('这个只读属性, 不能设置数据')
        # 2 如果不是, 真正的添加进去
        else:
            # self.key = value 这样写满足上面的当..时, 自动调用会进入死循环, 用下面.__dict__方法
            self.__dict__[key] = value


p1 = Person()
p1.age = 20
p1.name = 'd'
p1.age = 30
print(p1.__dict__)  # 显示并没有真正添加这个属性
