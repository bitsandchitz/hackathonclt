"""projectruben URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from ruben import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^unit/$', views.unit_list),
    url(r'^unit/(?P<pk>[0-9]+)$', views.unit_detail),
    url(r'^tenant/$', views.tenant_list.as_view()),
    url(r'^tenant/(?P<pk>[0-9]+)$', views.tenant_detail.as_view()),
]
