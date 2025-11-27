class Text():
    def t(self):
        print('ttttt')

    def close(self):
        print('资源释放')

#   def __enter__(self):
#       return self
#
#   def __exit__(self, exc_type, exc_val, exc_tb):
#       self.close()


import contextlib
# contextlib.closing函数让一个拥有close方法但不是上下文管理器的对象变成上下文管理器
with contextlib.closing(Text()) as x:
    x.t()
