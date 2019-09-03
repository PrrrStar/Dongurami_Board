# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from myapp.models import myapp
# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model = myapp
        fields = ['id', 'title', 'author']

def post_list(request, template_name='myapp/post_list.html'):
    posts = myapp.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_add(request, template_name='myapp/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myapp:post_list')
    return render(request, template_name, {'form': form})

def post_edit(request, pk, template_name='myapp/post_form.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('myapp:post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, pk, template_name='myapp/post_delete.html'):
    post = get_object_or_404(myapp, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('myapp:post_list')
    return render(request, template_name, {'object': post})