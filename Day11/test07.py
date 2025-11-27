accounts = ['张三', '李四', '王五', '刘六']

user = input('请输入您的名称:')

# 判断一个对象是否属于另一个对象  in/not in
if user in accounts:
    print(f'{user}已存在列表')
else:
    print(f'{user}不存在')
    # 添加
    accounts.append(user)
    print(f'{user}添加成功')
print(accounts)