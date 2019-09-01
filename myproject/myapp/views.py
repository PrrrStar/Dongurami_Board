from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from myapp.models import boardConf
from myapp.forms import boardForm


# Create your views here.

def index(request):
    
    list_from_db = boardConf.objects.all()
    context = {'list_from_db' : list_from_db}
    return render(request, 'index.html', context)

def add(request):

    if request.method == 'POST':
        form = boardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form = boardForm()
    return render(request,'add.html', {'form': form})

def detail(request, pk):
    err = get_object_or_404(boardConf, pk=pk)
    return render(request, 'detail.html', {'err':err})

def edit(request, pk):
    err = get_object_or_404(boardConf, pk=pk)
    
    if request.method == 'POST':
        form = boardForm(request.POST, instance=err)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = boardForm(instance = err)
        return render(request,'edit',{'form':form})

def delete(request, pk):
    list_from_db = boardConf.objects.get(pk=pk)
    list_from_db.delete()
    return redirect('index')
 