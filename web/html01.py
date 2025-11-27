from flask import Flask, render_template,request

# template_folder='文件夹名' 去当前项目的文件夹名找
app = Flask(__name__, template_folder='templates')


@app.route("/show/info")
def index():
    # return "中<h1>国</h1><span style='color:red;'>联通</span>"
    # Flask内部会自动打开这个文件, 并读取内容, 将内容给用户返回
    # 默认: 去当前项目目录的templates文件夹中找
    return render_template("index.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


@app.route("/user/list")
def user_list():
    return render_template("user_list.html")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route('/do/reg', methods=['GET'])
def do_register():
    # 接收用户通过GET发送过来的数据
    print(request.args)
    # 返回结果给用户
    return '注册成功'


if __name__ == '__main__':
    app.run()
