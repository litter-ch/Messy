# 采集的数据
values = (5, 6, 8, 9)

# 平均数
mean = sum(values) / len(values)
print(f'平均值: {mean}')

# 变异数(数学里的方差)
viriance = 0
for value in values:
    viriance += pow((value - mean), 2)
viriance = viriance / len(values)
print(f'变异数: {viriance}')

# 标准偏差(数学里的标准差)
deviation = pow(viriance, 1/2)
print(f'标准偏差: {deviation}')