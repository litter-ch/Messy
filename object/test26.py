# 面向对象-切片操作
class Person(object):
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __setitem__(self, slice, value):
        self.items[slice] = value

    def __getitem__(self, slice):
        print(p.items[slice])
        print('d')

    def __delitem__(self, slice):
        del self.items[slice]


p = Person()
p[0:4:2] = ['a', 'b']
print(p.items)

p[::2]

del p[0:4:2]
print(p.items)
