import functools


# 自动补全剩余的比较操作
@functools.total_ordering
class Person:
    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass



