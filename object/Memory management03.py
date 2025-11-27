# objgraph.count() 可以查看垃圾回收器跟踪的个数
class Person:
    pass

class Dog:
    pass

import objgraph
import gc
p = Person()
d = Dog()
print(objgraph.count('Person'))
print(objgraph.count('Dog'))
# 让两个实例对象互相引用, 造成循环引用
# 弱引用或者破坏循环引用也可以解决
# 弱引用:
# import weakref
# p.pet = weakref.ref(d)
# 破坏循环引用: p.pet = None
p.pet = d
d.master = p
# 删除可到达引用之后, 引用计数器机制无法回收
del p
del d
# 使用垃圾回收机制回收循环引用
# 手动触发, 关闭垃圾回收机制照样触发
gc.disable()
gc.collect()

print(objgraph.count('Person'))
print(objgraph.count('Dog'))
