
"""
crudapp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.urls import path
from django.contrib import admin
from myapp import views

urlpatterns = [
    path(r'^$', views.post_list, name='post_list'),
    path(r'^new$', views.post_add, name='post_new'),
    path(r'^edit/(?P<pk>\d+)$', views.post_edit, name='post_edit'),
    path(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
]