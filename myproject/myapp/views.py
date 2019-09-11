# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm, Textarea
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Board_DB, Comment_DB

# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model = Board_DB
        fields = ['id', 'title', 'writer','contents','pwd']

class CommentForm(ModelForm):
    class Meta:
        model = Comment_DB
        fields = ['id','c_contents']
        widgets={
            'c_contents':Textarea(attrs={'cols':60,'rows':2}),
            
        }
        
    
def post_list(request):
    posts = Board_DB.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, 'myapp/post_list.html', data)

def post_detail(request, pk):
    post = get_object_or_404(Board_DB, pk=pk)
    print(post)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            #  comment.c_writer = request.user
            comment.c_post = post
            comment.save()
            return redirect('post_detail', pk= pk)
    return render(request, 'myapp/post_detail.html', {'post':post, 'form':form})

def comment_like(request, pk):
    comment = get_object_or_404(Comment_DB, c_pk=c_pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment.c_like +=1
        comment.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'myapp/post_detail.html', {'comment':comment, 'form':form})

def post_add(request, template_name='myapp/post_add.html'):
    form = PostsForm(request.POST or None)
    contents = form
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Board_DB, pk=pk)
    post.delete()
    return redirect('post_list')

def comment_delete(request, pk, c_pk):
    comment = get_object_or_404(Comment_DB , c_pk = c_pk)
    comment.delete()
    return redirect('post_detail', pk=pk)


def comment_dislike(request, pk):
    post = get_object_or_404(Board_DB, pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment.c_like -=1
        comment.save()
        return redirect('post_detail', pk= pk)
    return render(request, 'myapp/post_detail.html', {'post':post, 'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Board_DB, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():  
        form.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'myapp/post_edit.html', {'form': form})
