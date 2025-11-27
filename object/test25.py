# 面向对象-索引操作
class Person:
    # 定义一个字典来接受后面的操作
    def __init__(self):
        self.cache = {}

    # 增加或修改字典里的键值对
    def __setitem__(self, key, value):
        self.cache[key] = value

    # 查询字典里的键值对
    def __getitem__(self, key):
        return self.cache[key]

    # 删除字典里的键值对
    def __delitem__(self, key):
        del self.cache[key]


p = Person()
p['name'] = 'Jack'

print(p['name'])

del p['name']
