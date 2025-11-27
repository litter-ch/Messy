# 类对象的创建方式
# type(类名,父类元组,类属性字典)

def run(self):
    print(self)


# 创建了一个dog 类
xxx = type('dog', (), {'count': 0, 'run': run})
print(xxx)
print(xxx.__dict__)

d = xxx()
print(d.__dict__)

# 1.检测类中是否有__metaclass__属性
# 2.检测父类中是否有__metaclass__属性
# 3.检测模块中是否有__metaclass__属性
# 4.通过内置的type这个元类来创建这个类对象
