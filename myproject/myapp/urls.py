
"""
crudapp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.post_list, name='post_list'),
    path(r'^post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path(r'^post_add', views.post_add, name='post_add'),
    path(r'^/post_edit/<int:pk>', views.post_edit, name='post_edit'),
    path(r'^/post_delete/<int:pk>', views.post_delete, name='post_delete'),

    path(r'^c_delete/<int:c_pk>', views.comment_delete, name='comment_delete'),
    path(r'^c_like/<int:c_pk>', views.comment_like, name='comment_like'),
    path(r'^c_dislike/<int:c_pk>', views.comment_dislike, name='comment_dislike'),
    
]