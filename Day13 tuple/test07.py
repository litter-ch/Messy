chongqing = ['渝北区', '江北区', '南岸区', '合川区', '涪陵区']
shanghai = ['黄浦区', '浦东新区', '静安区', '徐汇区', '长宁区']
guangzhou = ['花都区', '番禺区', '南沙区', '天河区', '越秀区']

# 简便的元组方式
china = chongqing, shanghai, guangzhou
print(china, type(china))

# 元组中的元素不能更改, 列表里的是可以更改的
# 可以改变元组里的列表
chongqing.append('纽约区')
shanghai.append('曼哈顿区')
guangzhou.append('白宫区')
print(china, type(china))
