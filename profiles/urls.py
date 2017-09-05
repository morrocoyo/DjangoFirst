from django.conf.urls import url, include


from .views import ProfileDetailView

from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

app_name ='profiles'
urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
    ]