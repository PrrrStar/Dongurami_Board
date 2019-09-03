# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from myapp.models import myDB
# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model = myDB
        fields = ['id', 'title', 'writer']


def post_list(request, template_name='myapp/index2.html'):
    posts = myDB.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_detail(request, template_name='myapp/post_detail.html'):
    posts = myDB.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_add(request, template_name='myapp/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form': form})

def post_edit(request, pk, template_name='myapp/post_form.html'):
    post = get_object_or_404(myDB, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, pk, template_name='myapp/post_delete.html'):
    post = get_object_or_404(myDB, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, template_name, {'object': post})