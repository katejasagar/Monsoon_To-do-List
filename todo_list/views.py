from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo_list
from .forms import *
# Create your views here.
def home(request): #To return what users will see
    tasks = todo_list.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks' : tasks,
        'form' : form,
    }
    return render(request, 'todo_list/home.html',context)

def update_task(request,pk):
    task = todo_list.objects.get(id = pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'todo_list/update.html',context)

def delete_task(request,pk):
    item = todo_list.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'todo_list/delete.html',context ) 