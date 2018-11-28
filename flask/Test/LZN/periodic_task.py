from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379')

# 添加定时任务
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(3.0, test.s("hello"), name='每隔3秒调用一次')
    sender.add_periodic_task(3.0, test.s("world"), expires=10)
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s("Happy Mondays!"),
    )
# celery -A periodic_task beat 开一个进程
# celery -A periodic_task worker


@app.task
def test(arg):
    print(arg)