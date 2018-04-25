from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^bike$', views.bike_list, name='bike_list'),
    # ex: /wine/5/
    url(r'^bike/(?P<bike_id>[0-9]+)/$', views.bike_detail, name='bike_detail'),
    url(r'^bike/(?P<bike_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]