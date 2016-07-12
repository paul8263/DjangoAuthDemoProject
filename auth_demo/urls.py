"""auth_demo URL Configuration

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
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', views.index, name='index'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    url(r'^accounts/profile/$', views.profile),
    url(r'^accounts/password_change/$', auth_views.password_change, {'template_name': 'password_change.html'},
        name='password_change'),
    url(r'^accounts/password_change/done/$', auth_views.password_change_done,
        {'template_name': 'password_change_done.html'}, name='password_change_done'),
    url(r'^accounts/password_reset/$', auth_views.password_reset,
        {'template_name': 'password_reset.html', 'subject_template_name': 'password_reset_subject.txt',
         'email_template_name': 'password_reset_email.html'}, name='password_reset'),
    url(r'^accounts/password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(
        r'^accounts/password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^accounts/password_reset/complete/$', auth_views.password_reset_complete,
        {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),
]
