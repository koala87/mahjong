"""mahjong URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create', views.create_view),
    url(r'^list', views.list_view),
    url(r'^record/(\d+)', views.record_view),
    url(r'^show/(\d+)', views.show_view),
    url(r'^rule', views.rule_view),
    url(r'^member', views.member_view),
    url(r'^random', views.random_view),
    url(r'^.*$', views.member_view),
]