#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : 2020/7/8 下午2:48 
@Author : ztoben
@Desc   :
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url('index/', views.index),
    url('upload/', views.upload),
    url('rank/', views.rank)
]