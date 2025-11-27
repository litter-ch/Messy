def my_car(cars, func):
    for car in cars:
        # 调用 func 函数, 将 car 作为参数传入
        print(func(car))


def dream_car(brand):
    return 'My dream is ' + brand


# 主函数
brands = ['仰望U8', '蔚来ES8', '红旗H9']
my_car(brands, dream_car)

print('-' * 20)

# 使用 lambda 匿名函数作为参数传递
my_car(brands, lambda c: 'My car is ' + c)

