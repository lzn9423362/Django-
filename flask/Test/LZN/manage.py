from flask import Flask
from tasks import send_mail
app = Flask(__name__)

@app.route('/')
def hello():
    send_mail.delay('41112080@qq.com')
    return '哈哈'


if __name__ == '__main__':
    app.run()
