t_shirt = float(input('请输入t_shirt的单价:'))
pants = float(input('请输入裤子的单价:'))

t_shirt_count = int(input('买了几件t_shirt:'))
pants_count = int(input('买了几件裤子:'))

sum1 = t_shirt * t_shirt_count
sum2 = pants * pants_count
sum = sum1 +sum2
money = sum *0.88
52
print(f'一共{sum}元')
print(f'今天老板生日打88折，现在只要{money}元')