# 2.3版本-2.7版本  新式类使用C3算法(经典类不变)
# C3算法:
# L(object) = [object]
# L(子类(父类,..,父类n)) = [子类] + merge(L(父类1),L(父类2), ..,L(父类n),  [父类1,...,父类n])
# merge算法:1. 第一个列表的第一个元素是后续所有列表的第一个元素 或 后续所有列表中没有再次出
#             现, 则将这个元素合并到最终解析列表中, 并从当前操作列表的所有列表中删除
#          2. 不符合则跳过此元素, 查找下一个列表的第一个元素, 重复1的操作
#          3. 如果最终无法把所有元素归并到解析列表, 则报错
class D(object):
    pass
# L(D(object)) = [D] + merge(L(object), [object])
#              = [D] + merge([object], [object])
#              = [D, object] + merge([], [])
#              = [D, object]
# L(D) = [D, object]


class B(D):
    pass
# L(B(D)) = [B] + merge(L(D), [D])
#         = [B] + merge([D, object], [D])
#         = [B, D] + merge([object], [])
#         = [B, D, object] + merge([], [])
#         = [B, D, object]
# L(B) = [B, D, object]


class C(D):
    pass
# L(C(D)) = [C] + merge(L(D), [D])
#         = [C] + merge([D, object], [D])
#         = [C, D] + merge([object], [])
#         = [C, D, object] + merge([], [])
#         = [C, D, object]
# L(C) = [C, D, object]


class A(B, C):
    pass
# L(A(B, C)) = [A] + merge(L(B), L(C), [B, C])
#            = [A] + merge([B, D, object], [C, D, object], [B, C])
#            = [A, B] + merge([D, object], [C, D, object], [C])
#            = [A, B, C] + merge([D, object], [D, object], [])
#            = [A, B, C] + merge([D, object], [D, object], [])
#            = [A, B, C, D] + merge([object], [object])
#            = [A, B, C, D, object] + merge([], [])
#            = [A, B, C, D, object]
# L(A) = [A, B, C, D, object]


import inspect
print(inspect.getmro(A))
