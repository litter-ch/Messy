class Person(object):

    # 将对象作为函数被调用时触发
    def __call__(self, *args, **kwargs):
        print('xxx', args, kwargs)

    pass


p = Person()

p(123, 456, name='Jack')
