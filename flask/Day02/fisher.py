# 从ｆｌａｓｋ框架中导入Ｆｌａｓｋ这个类
from flask import Flask
#初始化一个ｆｌａｓｋ对象
#需要传递一个参数__name__
# 1.方便ｆｌａｓｋ框架去寻找资源
# 2.方便flask插件比如ｆｌａｓｋ-Sqlalchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

#如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    #启动一个应用服务器，来接受用户的请求
    app.run(host='0.0.0.0')