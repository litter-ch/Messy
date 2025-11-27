class Person:
    def __init__(self):
        self.age = 20
        self.name = '彭于晏'
        self.sex = '男'

    # 访问的属性不存在的时候触发
    def __getattr__(self, item):
        print('getattr方法被触发')
        return '吴彦祖'

    # 相当于在重载object中的__setattr__
    def __setattr__(self, attr_name, value):
        if attr_name == 'sex' and value in ['男', '女']:
            object.__setattr__(self, attr_name, value)
        else:
            pass


p = Person()
print(p.age)
print(p.name)
print(p.ag)
p.sex = '女'
print(p.sex)
