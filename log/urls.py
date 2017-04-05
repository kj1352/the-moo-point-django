#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post',views.post, name='post'),
    url(r'^see', views.see, name="see"),
]
