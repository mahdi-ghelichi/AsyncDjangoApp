from App.tasks import process
from App.models import Tasks
from App.forms import JobForm
from django.shortcuts import render
from celery.result import AsyncResult
from django.views.decorators.http import require_http_methods, require_GET


@require_http_methods(["GET", "POST"])
def run(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            job_name = data['job_name']
            process.delay(job_name=job_name)
            return render(request, 'job.html',
                          context={'form': JobForm,
                                   'message': f'{job_name} dispatched...'})
    else:
        return render(request, 'job.html', context={'form': JobForm})


def track_jobs():
    entries = Tasks.objects.all()
    information = []
    for item in entries:
        progress = 100  # max value for bootstrap progress bar, when the job is finished
        result = AsyncResult(item.task_id)
        if isinstance(result.info, dict):
            progress = result.info['progress']
        information.append([item.job_name, result.state, progress, item.task_id])
    return information

@require_GET
def monitor(request):
    info = track_jobs()
    return render(request, 'monitor.html', context={'info': info})

@require_GET
def cancel_job(request, task_id=None):
    result = AsyncResult(task_id)
    result.revoke(terminate=True)
    info = track_jobs()
    return render(request, 'monitor.html', context={'info': info})


@require_GET
def delete_job(request, task_id=None):
    a = Tasks.objects.filter(task_id=task_id)
    a.delete()
    info = track_jobs()
    return render(request, 'monitor.html', context={'info': info})
