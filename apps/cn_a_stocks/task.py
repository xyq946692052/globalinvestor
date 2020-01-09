import time

from celery.task.schedules import crontab
from celery.decorators import periodic_task

from globalinvestor import celery_app


@periodic_task(run_every=10)
def some_task():
    print('++++periodic task test!!!')
    time.sleep(1)
    print('---some_task success')
    return True


@celery_app.task
def sendmail(email):
    import time
    print('start send email to {}'.format(email))
    time.sleep(10)
    print('---send success')
    return True
