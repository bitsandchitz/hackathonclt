from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^unit/$', views.unit_list),
    url(r'^unit/(?P<pk>[0-9]+)$', views.unit_detail),
    url(r'^tenant/$', views.tenant_list.as_view()),
    url(r'^tenant/(?P<pk>[0-9]+)$', views.tenant_detail.as_view()),
]
'''