# 制作冰淇淋
# * 表示可以接受多个参数(任意数量) args => arguments 形式参数(形参)
# 一般参数与任意参数结合的参数列表
def make_icecream(icecream_type, *args):
    ''' 列出冰淇淋的佐料 '''
    print(icecream_type)
    print(f'{args=}, {type(args)=}')
    print(f'冰淇淋添加的配料如下:')
    for topping in args:
        print(topping)


make_icecream('香草', '草莓酱')
print('-' * 50)
make_icecream('芒果', '草莓酱', '葡萄干', '巧克力碎片')
print('-' * 50)
make_icecream('香草', '草莓酱')