from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import TodoForm,CreateUserForm
from .models import todos

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account has been created for ' + user)
                return redirect('login')

        context = {
            'form': form
        }

        return render(request,'todos/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        context = {}
        return render(request,'todos/index.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homeView(request):
    form = TodoForm()
    user =request.user
    mytodo = user.todo.all()
    context = {
        'form' : form,
        'mytodo': mytodo
    }
    return render(request,'todos/home.html',context)

@login_required(login_url='login')
def addTodo(request):
    form = TodoForm(request.POST)
    user = request.user
    if form.is_valid():
        my_new_todo = todos(todotext=request.POST['text'],user=user)
        my_new_todo.save()
    return redirect('home')

@login_required(login_url='login')
def completeTodo(request,todo_id):
    my_todo = todos.objects.get(pk=todo_id)
    my_todo.completed = True
    my_todo.save()
    return redirect('home')

@login_required(login_url='login')
def incompleteTodo(request,todo_id):
    my_todo = todos.objects.get(pk=todo_id)
    my_todo.completed = False
    my_todo.save()
    return redirect('home')

@login_required(login_url='login')
def deleteTodo(request,todo_id):
    my_todo = todos.objects.get(pk=todo_id)
    my_todo.delete()

    return redirect('home')

@login_required(login_url='login')
def deleteall(request):
    my_todo = todos.objects.all()
    for x in my_todo:
        x.delete()
    return redirect ('home')




