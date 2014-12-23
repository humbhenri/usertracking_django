from django.conf.urls import patterns, url

from userapp import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index.html$', views.IndexView.as_view(), name='index'),
    url(r'^create$', views.UserCreate.as_view(), name='create'),
    url(r'update/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.UserDelete.as_view(), name='delete'),
)