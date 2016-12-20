"""glotechsol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^about_us/', 'content.views.about_us'),
    url(r'^service/', 'content.views.service'),
    url(r'^portfolio/', 'content.views.portfolio'),
    url(r'^contact/', 'content.views.contact'),
    url(r'^getlang/(\d+)/$', 'content.views.getlang', name='getlang'),
    url(r'^details/(\d+)/(\d+)/$', 'content.views.details'),
    url(r'^details/(\d+)/$', 'content.views.details'),
    url(r'^news/(?P<content_id>\d+)/$', 'content.views.news'),
    url(r'^userauthenticate/$', 'content.views.userauthenticate', name='userauthenticate'),
    url(r'^usersignin/$', 'content.views.usersignin', name='usersignin'),
    url(r'^user_logout/$', 'content.views.user_logout', name='user_logout'),
    url(r'^lecca/(\d+)/$', 'content.views.lecca'),
    url(r'^(?P<error>\w+)/', 'content.views.get_news'),
    url(r'^$', 'content.views.get_news'),
]


