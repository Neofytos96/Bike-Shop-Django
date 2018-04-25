from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.bike_list, name='bike_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.bike_list, name = 'bike_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.bike_detail, name = 'bike_detail'),
]