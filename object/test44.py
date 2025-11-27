class Peron:
    # def __init__(self):
    #     print('init')
    count = []
    count_max = 3

    # 实例化对象之后触发
    def __init__(self):
        # 为对象添加对象属性
        self.name = '吴彦祖'
        self.sex = '男'

    def __getattribute__(self, item):
        print(item)  # item 为要访问的属性的字符串
        # 不能使用当前对象的属性访问, 会再次触发当前魔术方法进入递归循环!
        result = object.__getattribute__(self, 'name')
        # 隐藏用户名
        new_name = result[0] + '*' + result[-1]
        return new_name

    # 修改对象的创建过程
    def __new__(cls):
        # 在创建过程中执行
        if len(cls.count) < cls.count_max:
            cls.count.append(cls)
            instance = super().__new__(cls)
            print('创建了一个')
            return instance

    # 使用len函数检测对象的时候自动触发
    def __len__(self):
        print('__len__方法被触发')
        return len(self.count)

    def __str__(self):
        print('__str__方法被触发')
        return '掉包了'


p1 = Peron()
p2 = Peron()
p3 = Peron()
p4 = Peron()
p5 = Peron()
print(len(p1))
print(p1)
# 当前name属性被__getattribute__所截取
# 已经触发了属性访问顺序的第一个
print(p1.sex)

