from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from App.tasks import process
from django.shortcuts import render


@require_http_methods(["GET", "POST"])
@login_required
def run(request):
    if request.method == "POST":
        process.delay()
    else:
        pass
