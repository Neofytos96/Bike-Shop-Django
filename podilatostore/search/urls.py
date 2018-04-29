from django.conf.urls import url
from mysite.search import views

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
]