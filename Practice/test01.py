import tkinter

# 1.1 定义一个窗口对象
# root = tkinter.Tk()

# # 一页
# login_frame = tkinter.Frame(root)
# login_frame.grid()
#
# # 设置标题
# root.title('学生信息管理系统')
# root.geometry('300x180')
# tkinter.Label(login_frame, width=15).grid(column=0, row=0)
#
# username = tkinter.StringVar()
# password = tkinter.StringVar()
#
# tkinter.Label(login_frame, text='账户:').grid(row=1, column=0)
# tkinter.Entry(login_frame, textvariable=username).grid(row=1, column=1)
#
# tkinter.Label(login_frame, text='密码:').grid(row=2, column=0)
# tkinter.Entry(login_frame, textvariable=password).grid(row=2, column=1)
#
#
# # 点击登录 校验参数
# def check_login():
#     print('检查登录')
#     print('用户名:', username.get())
#     print('密码:', password.get())
#     if username.get() == 'hello' and password.get() == '123456':
#         print('登录成功')
#         # 换页
#         login_frame.destroy()
#     else:
#         print('登陆失败')
#
#
# tkinter.Button(login_frame, text='登录', command=check_login).grid(row=3, column=0)
# tkinter.Button(login_frame, text='退出', command=root.quit).grid(row=3, column=1)


class LoginPage:
    def __init__(self):
        # 初始化
        self.root = tkinter.Tk()

        self.login_frame = tkinter.Frame(self.root)
        self.login_frame.grid()

        # 设置标题
        self.root.title('学生信息管理系统')
        self.root.geometry('300x180')

        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.creat_page()
        self.root.mainloop()

    def creat_page(self):
        tkinter.Label(self.login_frame, width=15).grid(column=0, row=0)

        tkinter.Label(self.login_frame, text='账户:').grid(row=1, column=0)
        tkinter.Entry(self.login_frame, textvariable=self.username).grid(row=1, column=1)

        tkinter.Label(self.login_frame, text='密码:').grid(row=2, column=0)
        tkinter.Entry(self.login_frame, textvariable=self.password).grid(row=2, column=1)

        tkinter.Button(self.login_frame, text='登录', command=self.check_login).grid(row=3, column=0)
        tkinter.Button(self.login_frame, text='退出', command=self.root.quit).grid(row=3, column=1)

    # 点击登录 校验参数
    def check_login(self):
        print('检查登录')
        print('用户名:', self.username.get())
        print('密码:', self.password.get())
        if self.username.get() == 'hello' and self.password.get() == '123456':
            print('登录成功')
            # 换页
            self.login_frame.destroy()
        else:
            print('登陆失败')






login_page = LoginPage()
