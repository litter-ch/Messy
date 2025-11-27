import mysql.connector

# 直接连接数据库（请修改为你的数据库信息）
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # 你的MySQL用户名
        password='020903',  # 你的MySQL密码
        database='db1',  # 你的数据库名
        port=3306,
        charset='utf8'
    )
    print("数据库连接成功！")

    # 创建游标
    cursor = conn.cursor()

    # 查询数据
    cursor.execute("SELECT * FROM student ;")

    # 获取结果
    result = cursor.fetchall()
    for stu in result:
        print(stu)

    # 关闭连接
    cursor.close()
    conn.close()
    print("\n数据库连接已关闭")

except mysql.connector.Error as e:
    print(f"发生错误: {e}")
