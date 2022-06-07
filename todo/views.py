from email import message
from urllib import request
from django import views
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task
from todo.forms import TaskForm
from django.contrib import messages

# Create your views here.
def home(request):
    data = Task.objects.all()
    c_data = Task.objects.filter(completed=True)
    complete = c_data.count()
    total_task = data.count()
    
    return render(request, 'index.html', {'data':data, 'total_complete':complete,"total_task":total_task})

def today_view(request):
    data = Task.objects.all()


    return render(request, 'today.html', {'datalist':data, 'today':today,'tdata':today_data})


def create(request):
    data = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Task Added Successfully!')
            return redirect('home')

    return render( request, 'newtask.html', {'form':form, 'data':data})

def viewall(request):
    data = Task.objects.all()

    return render(request, 'alltask.html', {'data':data})


def completed(request):
    data = Task.objects.all()
    c_data = Task.objects.filter(completed=True)
    complete = c_data.count()

    return render(request, 'completed.html', {'c_data':c_data, 'data':data,"total_complete" : complete})

def viewone(request, pk):
    field = get_object_or_404(Task, pk=pk)
    data = Task.objects.all()
    return render(request, 'viewone.html', {'field':field,'data':data})

def edit(request, pk):
    data = Task.objects.all()
    field = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=field)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=field)

        if form.is_valid():
            form.save()
            messages.info(request, 'Task edited!!')
            return redirect('home')
    return render(request, 'newtask.html', {'form':form,'data':data})    

def tdel(request, pk):
    data = get_object_or_404(Task, pk=pk)
    data.delete()
    return redirect('home')