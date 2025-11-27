# 添加20之内的勾股数

# for a in range(1,21):
#     a += 1
#     for b in range(a,21):
#         b += 1
#         for c in range(b,21):
#             if pow(a, 2) + pow(b, 2) == pow(c, 2):
#                 print(f'{a=}, {b=}, {c=}')

list3 = [[a, b, c] for a in range(1, 21) for
         b in range(a, 21) for c in range(b, 21)
         if pow(a, 2) + pow(b, 2) == pow(c, 2)]
print(f'{list3=}')

for a, b, c in list3:
    print(f'{a=}, {b=}, {c=}')

