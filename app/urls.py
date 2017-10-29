
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup/$', views.signup, name='form'),
    url(r'^signup/post/$', views.post_user, name='post_user'),
    url(r'^signin/$', views.signin, name='form'),
    url(r'^signin/login/$', views.authentication, name='authentication'),
    url(r'^logout/$', views.logout, name='logout'),

]

# Add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve,
           {'document_root':settings.MEDIA_ROOT,}),
]
