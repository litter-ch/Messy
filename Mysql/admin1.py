import mysql.connector

# 连接数据库
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # MySQL用户名
        password='020903',  # MySQL密码
        database='unicom',  # 数据库名
        port=3306,
        charset='utf8'
    )
    dbname = 'unicom'
    print(f"数据库{dbname}连接成功！")
    print('q 是退回上次命令直至退出程序')

    # 创建游标
    cursor = conn.cursor()
    while True:
        request = input('请输入您的请求,增加(insert)查询(find)或其他命令(else)): ')
        if request == 'q':
            break
        try:
            if request.lower() == 'find':  # 查询命令
                while True:
                    command = input('请输入sql语句查询命令: ')
                    if command.lower() == 'q':
                        break
                    else:
                        if 'select' or 'show' in command.lower():
                            try:
                                # 查询数据
                                cursor.execute(command)
                                # fetchall获取所有结果
                                # fetchone获取第一个结果
                                result = cursor.fetchall()
                                for stu in result:
                                    print(stu)
                            except mysql.connector.Error as err:
                                print(err)
                        else:
                            print('输入有误')
            elif request.lower() == 'insert':  # 添加命令
                while True:
                    username = input('用户名: ')
                    if username.lower() == 'q':
                        break
                    password = input('密码: ')
                    mobile = input('号码: ')
                    if len(mobile) == 11:
                        sql = 'insert into admin1(username,password,mobile) values(%s, %s, %s)'
                        cursor.execute(sql, [username, password, mobile])
                        conn.commit()
                        print('成功添加')
                    else:
                        print('号码输入错误')

            elif request.lower() == 'else':  # 其他命令
                while True:
                    command = input('请输入sql语句命令: ')
                    if command.lower() == 'q':
                        break
                    try:
                        cursor.execute(command)
                        conn.commit()
                    except mysql.connector.Error as err:
                        print(err)
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
