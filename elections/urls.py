from django.conf.urls import url

from . import views

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/results/$', views.results),
	url(r'^areas/(?P<area>.+)/$', views.areas),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]