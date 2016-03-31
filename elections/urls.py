from django.conf.urls import url

from . import views

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]