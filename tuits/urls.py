from django.conf.urls import url


from .views import (
        TuitListView,
        TuitDetailView,
        TuitCreateView,
        TuitUpdateView
        )

app_name='tuits'            #esto fue clave
urlpatterns = [
    url(r'^create/$', TuitCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', TuitUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', TuitUpdateView.as_view(), name='detail'),
    url(r'$', TuitListView.as_view(), name='list'),
    ]