from flask import Flask

app = Flask(__name__) #初始化flask对象，yong__name__来确定程序根目录


#注明通过什么样的url可以访问函数，同时在函数中返回要显示在浏览器中的信息
"""上面的代码指定了url与python函数的映射关系，我们把处理URL和函数间的关系定义为路由，把被装饰的函数
注册为路由，此处注册给index()函数的路由为根目录"""
@app.route('/')

def hello_world():
     return 'hello world'
"""这里的index()函数叫做视图函数，必须要有返回值，返回价值为字符串或简单的html页面等内容"""
if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=8888)
