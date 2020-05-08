# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:20:18 2020

@author: ATHITHIYA
"""

from django.conf.urls import url
from.import views

app_name='blog'
urlpatterns = [
    url(r'^list/$',views.blog_list,name="list"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login, name="login"),
    url(r'^donor/$', views.donor, name="donor"),
    url(r'^main/$', views.main, name="main"),
   # url(r'^(?P<slug>[\w-]+)/$', views.article_detail,name="detail"),
    ]