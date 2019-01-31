from AsyncDjangoApp.celery import app
from App.models import Tasks
from time import sleep
import random


@app.task(bind=True)
def process(self, job_name=None):

    b = Tasks(task_id=self.request.id, job_name=job_name)
    b.save()

    self.update_state(state='Dispatching', meta={'progress': '33'})
    sleep(random.randint(5, 10))  # pre-processing the dataset in machine learning pipeline,...

    self.update_state(state='Running', meta={'progress': '66'})
    sleep(random.randint(5, 10))  # training the algorithm,...

    self.update_state(state='Finishing', meta={'progress': '100'})
    sleep(random.randint(5, 10))  # reporting metrics, saving the model,...

