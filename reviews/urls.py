from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.add_review, name='add_review'),
    #url(r'^bike/(?P<bike_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]