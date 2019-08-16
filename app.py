from flask import Flask
from pass331 import passofflinelessons
from passlevel import pass_whole_progress
from flask import Flask, request, redirect, url_for, render_template, Response, jsonify, make_response
from L0pass import passofflineclasses

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("331.html")


@app.route('/passprogress')
def passprogress():
    return render_template("progress.html")


@app.route('/l0')
def L0progress():
    return render_template("L0progress.html")


@app.route('/test1')
def test1():
    return render_template("test1.html")


@app.route('/test4')
def test4():
    return render_template("test4.html")


@app.route('/test6')
def test6():
    return render_template("test6.html")


@app.route('/accounts', methods=['GET'])
def get_accounts():
    if request.method == "GET":

        username = request.args.get("account")
        if username == "":
            password = "Error! Please input memberid"

        else:

            passofflinelessons(username)
            # if password == "":
            #     return "no result"
            # else:
            #     #return render_template("home.html",message=username,password=password)
            #     return jsonify({"password": password})
            password = "Done!"
        return jsonify({"password": password})


@app.route('/progress', methods=['GET'])
def get_progress():
    if request.method == "GET":

        memberid = request.args.get("memberid")
        env = request.args.get("env")

        if memberid == "":
            message = "Error! Please input memberid"

        if env == "":
            messsage = "Error! Please select env"

        if memberid and env:
            pass_whole_progress(env, memberid)
            message = "Done"

        return jsonify({"result": message})


@app.route('/l0progress', methods=['GET'])
def get_l0_progress():
    if request.method == "GET":
        args =request.args
        memberid = request.args.get("memberid")
        env = request.args.get("env")
        select_all = request.args.get("all")
        choice = request.args.get("choice")

        if memberid == "":
            message = "Error! Please input memberid"
            return

        if env == "":
            messsage = "Error! Please select env"
            return

        if env in ["mobilefirst", "mobiledev", "uat"]:
            message = "Have Done!"

        else:
            message = "Current env cannot execute, please insert into db"

        if choice:
            my_list = choice


        else:
            my_list = [i for i in range(10)]

        if (select_all or choice) and memberid and env:
            sqlresult = passofflineclasses(env, memberid, my_list)

        return jsonify({"message": message, "result": sqlresult})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#
# @app.route('/new',methods=['POST'])   //第一个参数是路由，第二个是请求方法
# def new():
#     recv_data = request.get_data()  //得到前端传送的数据
#     print(recv_data)
#     data = somefunction()   //对数据做某些处理
#     return data

#
# $.ajax({
#                 url: "/new",   //对应flask中的路由
#                 type: "POST", //请求方法
#                 data: 'hello',   //传送的数据
#                 dataType: "json", //传送的数据类型
#                 success: function (data) {  //成功得到返回数据后回调的函数
#                     console.log(data)
#                 }
#             })
