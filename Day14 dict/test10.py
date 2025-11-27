# 字典内键的值是列表
sports = {'Jack': ['健身', '游泳'],
          'James': ['羽毛球', '足球', '乒乓球'],
          'Lucy': ['踢毽子', '跳绳'],
          'Rose': ['跳绳', '游泳', '跑步']}

# 元素的遍历
for name, hobbies in sports.items():
    print(f'{name}喜欢的运动是: ')
    # hobbies 是一个列表数据
    for hobby in hobbies:
        print(hobby)