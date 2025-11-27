import pymysql
from pymysql.cursors import DictCursor

# 1.连接mysql
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password="020903",
    database='unicom2',
    charset="utf8")
# DictCursor 查询结果封装为字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令
# cursor.execute("insert into admin(username,password,mobile) values('Jack','123456','13589641148')")
# conn.commit()

cursor.execute("select * from admin")
# fetchall获取所有结果
# fetchone获取第一个结果
data_list = cursor.fetchall()
for data in data_list:
    print(data)

# 3.关闭
cursor.close()
conn.close()
