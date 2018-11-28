from flask import Flask
# from config import DEBUG
#

from flask_script import Manager

app = Flask(__name__)
manage = Manager(app)

app.config.from_object('config')
print(app.config['DEBUG']) #默认ＤＥＢＵＧ就是Ｆａｌｓｅ,　config.py中没有设置ＤＥＢＵＧ就是Ｔｒｕｅ
@app.route('/index')#装饰器路由注册
@app.route('/')
def hello():
    return 'Hello World!'
#

app.add_url_rule('/hello', view_func=hello) #普通路由注册

#字典,dict 子类a
#if __name__ == '__main__':判断保证再生产环境下面不会加载flask自带的服务器
if __name__ == '__main__':
    #生产环境 nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5001) #该端口,host让外网可以访问
    # manage.run() #python run.py runserver -h 0 -p 5001 -d