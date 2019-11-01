from flask import Flask,url_for

app = Flask(__name__) #flask初始化

@app.route("/") #定义路由

def index():
    #定义视图函数
    url1 = (url_for('news',id='10086'))
    #视图函数名为参数，进行反转
    return "url反转内容为：%s" %url1

@app.route('/news/<id>')

def news(id):
    return u'您请求的参数是:%s' %id

if __name__ == '__main__':
    app.run(debug=True)