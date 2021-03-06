"""entry URL Configuration"""
from django.contrib import admin
from django.urls import path,include

from entry import settings
from . import views
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('',views.index,name='index'),
    path('director/',include('director.urls')),
    path('gaurd/',include('gaurd.urls')),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
