from flask import Flask
from App.views import init_blue
from App.exts import init_exts
from App.settings import env


# 初始化app
def init_app():
    # 创建flask应用app
    app = Flask(__name__)

    # 添加配置信息
    app.config.from_object(env.get('development'))
    # print(app.config)


    # 初始化插件
    init_exts(app)

    # 初始化蓝图
    init_blue(app)

    return app


