from django.conf.urls import url
from App import views

app_name = 'App'

urlpatterns = [
    url(r'^run/$', views.run, name='run'),
    url(r'^monitor/$', views.monitor, name='monitor'),
    url(r'^delete_job/(?P<task_id>.+)/$', views.delete_job, name='delete_job'),
    url(r'^cancel_job/(?P<task_id>.+)/$', views.cancel_job, name='cancel_job')
]
