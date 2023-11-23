from celery import Celery
from time import sleep


#  ** remaining work (celery -A runner inspect active)
#  ** start-worker (celery -A runner worker --loglevel=info)


# cache = StrictRedis(host="localhost", port=6379, db=0)
app = Celery('tasks', broker='redis://localhost:6379/0', backend='rpc://')

@app.task
def hello(task_id):
    sleep(5)
    print(f'hello world {task_id}')
