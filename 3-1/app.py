from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html') #使用render_template方法渲染模板

@app.route('/user/<username>')
def user(username):
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)