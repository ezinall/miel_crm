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

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^panel/$', views.panel_view, name='panel'),
    url(r'^objects/$', views.objects_view, name='objects'),
    url(r'^calendar/$', views.calendar_view, name='calendar'),
    url(r'^news/$', views.news_view, name='news'),
    url(r'^docs/$', views.docs_view, name='docs'),
    url(r'^contacts/$', views.contacts_view, name='contacts'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^task_new/$', views.task_new, name='task_new'),
    url(r'^task_postpone/(?P<task_id>[0-9]+)$', views.task_postpone, name='task_postpone'),
    url(r'^task_done/(?P<task_id>[0-9]+)$', views.task_done, name='task_done'),
    url(r'^task_del/(?P<task_id>[0-9]+)$', views.task_del, name='task_del'),
    url(r'^task_add_comment/(?P<task_id>[0-9]+)$', views.task_add_comment, name='task_add_comment')
]
