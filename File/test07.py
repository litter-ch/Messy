class Text:
    def __enter__(self):
        print('enter')
        return self

    # exc_type: 异常类型   exc_val: 异常值   exc_tb: 异常的追踪信息
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self, exc_type, exc_val, exc_tb)
        import traceback
        print(traceback.extract_tb(exc_tb))
        print('exit')
        return True


# with上下文管理器
# Text()创建了一个实例化对象
# as t 将Text类里enter方法的self赋值给了t
with Text() as t:
    print('hello', t)
    1 / 0
