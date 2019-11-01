from flask import Flask,url_for,redirect
#使用redirect来跳转到指定url

app = Flask(__name__)

@app.route('/')

def hello_world():
    print("首先访问了index这个视图函数")
    url1 = url_for('user_login')

    return redirect('/user_login')

@app.route('/user_login')

def user_login():
    return "这是登录界面，请登录"

if __name__ == '__main__':
    app.run(debug=True)
