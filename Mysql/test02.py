import mysql.connector

# 连接数据库

database = input('选择您的数据库进入: ')

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # 你的MySQL用户名
        password='020903',  # 你的MySQL密码
        database=database,  # 你的数据库名
        port=3306,
        charset='utf8'
    )
    print("数据库连接成功！")

    # 创建游标
    cursor = conn.cursor()

    request = input('请输入您的请求,增删改(else)查(find)): ')

    try:
        if request == 'find':
            command = input('请输入sql语句查询命令: ')
            if 'select' or 'show' in command.lower():
                # 查询数据
                cursor.execute(command)
                # 获取结果
                result = cursor.fetchall()
                for stu in result:
                    print(stu)
            else:
                print('输入有误')
        elif request == 'else':
            command = input('请输入sql语句命令: ')
            cursor.execute(command)
            conn.commit()
        else:
            print('输入有误')

    # 捕获异常
    except mysql.connector.Error as err:
        print('sql语法错误')
        print(err)

    # 关闭连接
    cursor.close()
    conn.close()
    print("\n数据库连接已关闭")

except mysql.connector.Error as e:
    print(f"发生错误: {e}")
