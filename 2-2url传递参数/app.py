from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
     return '这是url传参演示！'

@app.route('/user/<name>')

def user_name(name):
     return "接受到的名称为: %s" % name

if __name__ == '__main__':
     app.run(debug=True)