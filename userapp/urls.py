from django.conf.urls import patterns, url

from userapp import views

urlpatterns = patterns('',
	url(r'^newuser$', views.add_new_user, name='newuser'),
	url(r'^new$', views.new, name='new'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index.html$', views.IndexView.as_view(), name='index'),
)