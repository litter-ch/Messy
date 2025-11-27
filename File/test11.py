def set_age(age):
    if age <= 0 or age > 200:
        # 手动抛出异常
        raise ValueError('age must be between 0 and 200')
    else:
        print('年龄设置为:', age)


set_age(-10)
