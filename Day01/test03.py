name = '小明'
print(f'我的名字叫', name)
print(f'我的名字叫{name}')
name2 = '小美'
age = 18
print(f'我的名字叫{name2},今年{age}岁')
student_id1 = '000001'
print(f'我的学号是{student_id1}')
student_id2 = 1
# Python 的 print 也能实现格式化输出，方法是使用 % 操作符，它会将左边的字符串当做格式字符串，将右边的参数代入格式字符串：
# %d整型占位符 %06 整型必须是6位数，不足用0补齐
print('我的学号是%06d' % student_id2)
# 多个变量一起赋值
price, weight, money = 9.00, 5.00, 45.00
print(f'苹果单价{price}元/斤,购买了{weight}斤,需要支付{money}元')
# 如果要带入多个参数，则需要用 () 包裹代入的多个参数，参数与参数之间用逗号隔开，参数的顺序应该对应格式字符串中的顺序
print('苹果单价%.1f元/斤,购买了%.2f斤,需要支付%.3f元' % (price, weight, money))
scale = '10.00%'
print('数据比例是%s' % scale)
#  end=空字符串 拼接在一起不换行
print('数据比例是', end='')
print(scale)

