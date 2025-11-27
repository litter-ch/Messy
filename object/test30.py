# 面向对象-遍历操作
class Person:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            # 抛出异常
            raise StopIteration('停止遍历')
        return self.result


p = Person()

for i in p:
    print(i)

