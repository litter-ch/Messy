class Factory:
    def __init__(self, pen_type):
        self.pen_type = pen_type

    def __call__(self, pen_color):
        print(f'创建了一个{self.pen_type},它的颜色为{pen_color}')


pen = Factory('铅笔')
pen('红')
pen('蓝')
pen('绿')

pen = Factory('钢笔')
pen('红')
pen('蓝')
pen('绿')
