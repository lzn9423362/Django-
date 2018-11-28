from flask import Flask, render_template, request, g

from utils import login_log

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    print(request.args.get('a'))
    return 'search'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111':
            #g:是专门用来保存用户的数据的
            #g对象在一次请求中的所有代码的地方，都是可以使用的.
            g.username = 'zhiliao'
            g.ip = 'xx'
            login_log()
            print(username,password)
            return '登录成功'
        else:
            return '没有该用户'
if __name__ == '__main__':
    app.run(debug=True,host='0')
