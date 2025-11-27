# 调用函数与调用方法的不同
def eat1():
    print(1)
    print(2)
    print(3)


# 函数的调用
eat1()


class Person():
    def eat2(self):
        print(1)
        print(2)
        print(3)


p = Person()

# 方法的调用
p.eat2()
