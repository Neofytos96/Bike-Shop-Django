from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.review_create, name='review_create'),
]