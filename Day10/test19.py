# 深复制需要先导入import copy模块
import copy

a = [1, 2, 3, [4, 5, 6]]
# 深复制 两个独立的空间对象,  里面包含的子空间对象也是独立的
# 格式:复制对象=copy.deepcopy(被复制对象)
b = copy.deepcopy(a)
print(f'id(a)={id(a)}\nid(b)={id(b)}')
print(f'{a=},{b=}')
print(f'{id(a[3])=},{id(b[3])=}')

# 外层元素不会联动
a.append(7)
print(f'{a=},{b=}')

# 深复制不会造成子元素的联动
a[3].append(8)
print(f'{a=},{b=}')
