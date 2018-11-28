import time

from celery import Celery

# 创建celery对象,设置任务队列使用redis
app = Celery('tasks', broker='redis://localhost:6379')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3.0, test.s('李四'))


@app.task
def test(name):
    print('hello+ %s' %name)

# 创建任务
@app.task
def add(a, b):
    time.sleep(5)
    n = a + b
    print(n)
    return n

@app.task
def send_mail(a):
    time.sleep(7)
    print('发送完成')


@app.task
def sub(a,b):
    n = a - b
    time.sleep(6)
    print(n)
    return n
if __name__ == '__main__':
    print('执行开始')
    add.delay(10, 5)
    sub.delay(1,2)
    print('程序执行结束')