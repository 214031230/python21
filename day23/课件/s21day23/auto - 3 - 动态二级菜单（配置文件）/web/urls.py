from django.conf.urls import url,include
from web.views import home

urlpatterns = [
    url(r'^index/', home.index),
]
