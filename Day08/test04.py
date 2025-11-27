# 将输出数据写入到文件中
# open()函数可以打开一个文件供读取或写入
# 打开文件(路径 + 文件名称)
# mode='wt' 表示写入文本文件, 每次执行都会覆盖掉之前文件的内容
fstream1 = open(r'C:\Users\鸡蛋\Desktop\output1.txt', mode='wt', encoding='utf-8')
print("Testing for output", file=fstream1)
# 关闭文件
fstream1.close()

# mode='a' 在文件中拼接新的数据, 不会造成原有数据的覆盖
fstream2 = open(r'C:\Users\鸡蛋\Desktop\output2.txt', mode='a', encoding='utf-8')
fstream2.write('Testing for output' + '\n')
# 关闭文件
fstream1.close()