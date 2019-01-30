from AsyncDjangoApp.celery import app
from App.models import Tasks
from time import sleep
import random


@app.task(bind=True)
def process(self, job_name=None):

    b = Tasks(task_id=self.request.id, name=job_name)
    b.save()

    self.update_state(state='Dispatching')
    n = random.randint(5, 10)
    sleep(n)

    self.update_state(state='Running')
    n = random.randint(5, 10)
    sleep(n)

    self.update_state(state='Finishing')
    n = random.randint(5, 10)
    sleep(n)
