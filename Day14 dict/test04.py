# 定义一个空字典
names = {}

# 字典的复制
fruits = {'西瓜': 15, '香蕉': 20, '水蜜桃': 25, '梨': 20, '火龙果': 30, '无花果': 20}
fruits_copy = fruits.copy()
print(f'{id(fruits)=}, {id(fruits_copy)=}')

# 查看字典的键值对(元素)的个数
len_ = len(fruits_copy)
print(f'{len_=}')

# 验证元素是否存在
key = input('请输入需要购买的水果名称:')
if key in fruits:
    print(f'{key} = {fruits[key]}')
else:
    print(f'没有该水果')