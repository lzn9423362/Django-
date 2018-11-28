from datetime import timedelta
from flask import Flask, session
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) #将ｓｅｓｓｉｏｎ改为７天
@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    #没有设置过期时间，那么默认是浏览器关闭后
    #如果设置permanent属性为Ｔｒｕｅ则一个月后消失
    session.permanent = True
    return 'Hello World!'

@app.route('/get/')
def get():
    return session.get('username', 'hah')

@app.route('/delete/')
def delete():
    # session.pop('username', '')
    session.clear()
    print(session.get('username', '猪头肉'))
    return 'success'



if __name__ == '__main__':
    app.run(debug=True)
