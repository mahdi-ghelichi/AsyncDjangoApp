from django.db import models


class Tasks(models.Model):
    task_id = models.CharField(max_length=50, null=True)
    job_name = models.CharField(max_length=50, null=True)
