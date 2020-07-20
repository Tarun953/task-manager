from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import TodoForm
from .models import todos

# Create your views here.
def homeView(request):
    form = TodoForm()
    mytodo = todos.objects.order_by('id')
    context = {
        'form' : form,
        'mytodo': mytodo
    }
    return render(request,'todos/home.html',context)

def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = todos(todotext=request.POST['text'])
        my_new_todo.save()
    return redirect('home')

def completeTodo(request,todo_id):
    my_todo = todos.objects.get(pk=todo_id)
    my_todo.completed = True
    my_todo.save()
    return redirect('home')

def incompleteTodo(request,todo_id):
    my_todo = todos.objects.get(pk=todo_id)
    my_todo.completed = False
    my_todo.save()
    return redirect('home')

def deleteTodo(request,todo_id):
    my_todo = todos.objects.get(pk=todo_id)
    my_todo.delete()

    return redirect('home')

def deleteall(request):
    my_todo = todos.objects.all()
    for x in my_todo:
        x.delete()
    return redirect ('home')
