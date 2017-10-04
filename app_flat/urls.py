"""miel_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'flat'
urlpatterns = [
    url(r'^new/$', views.flat_new, name='flat_new'),
    url(r'^view/(?P<flat_id>[0-9]+)/$', views.flat_view, name='flat_view'),
    url(r'^set_status/(?P<flat_id>[0-9]+)/(?P<status_id>[0-9]+)$', views.set_status, name='flat_set_status'),
]
