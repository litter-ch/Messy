score = int(input(f'输入你的成绩:'))
if score < 0 or score >100:
    print(f'异常')
elif score >= 90:
    print(f'优秀')
elif score >= 80:
    print(f'良好')
elif score >= 60:
    print(f'及格')
elif score < 60 and score >= 0:
    print(f'不及格')

print(f'陈旭结束')




