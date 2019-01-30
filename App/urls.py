from django.conf.urls import url
from App import views

app_name = 'App'


urlpatterns = [
    url(r'^run/$', views.run, name='run'),
    url(r'^monitor/$', views.monitor, name='monitor'),
]
