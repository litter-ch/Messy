# 语音播报
import win32com.client  # 导入模块

# 创建一个播报器对象
speaker = win32com.client.Dispatch('SAPI.spVoice')

# 通过播报器对象, 播放字符串
speaker.Speak('我是计算器')
speaker.Speak(f'{speaker.__class__.__name__}')


class Calculator:
    # 检查是不是数字
    def __check_num(func):
        def inner(self, n):
            if not isinstance(n, int):
                speaker.Speak(f'{n} must be an integer')
                raise TypeError(f'{n} must be an integer')
            return func(self, n)

        return inner

    # 播报器
    def __say(self, word):
        speaker.Speak(word)

    # 装饰出不同的播报器
    def __attribute(word=''):
        def __say_zsq(func):
            def inner(self, n):
                self.__say(word + str(n))
                return func(self, n)

            return inner

        return __say_zsq

    @__check_num
    @__attribute()
    def __init__(self, num):
        self.__result = num

    @__check_num
    @__attribute('加')
    def add(self, n):
        self.__result += n
        return self

    @__check_num
    @__attribute('减')
    def subtract(self, n):
        self.__result -= n
        return self

    @__check_num
    @__attribute('乘')
    def multiply(self, n):
        self.__result *= n
        return self

    @__check_num
    @__attribute('除')
    def divide(self, n):
        if n == 0:
            raise ZeroDivisionError('division by zero')
        self.__result /= n
        return self

    def clear(self):
        self.__result = 0
        return self

    def show(self):
        self.__say(f'结果为{self.__result}')
        print(self.__result)
        return self


# 链式编程
c = Calculator(3).add(4).subtract(1).multiply(4).divide(3).show()
