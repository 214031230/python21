from django.conf.urls import url, include
from web import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    
]
