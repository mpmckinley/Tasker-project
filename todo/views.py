from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm, RegisterForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        # return standard user form from Django
        return render(request, 'todo/signupuser.html', {'form':RegisterForm()})
    else:
        # make sure passwords match
        if request.POST['password'] == request.POST['password2']:
            try:
                # create user and add password
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                # add user to database
                user.save()
                # logon saved user
                login(request, user)
                # send logged on user back to current to do list
                return redirect('currenttodo')
            # if passwords match, check username to ensure unique, if not:
            except IntegrityError:
                # stores error and displays on signup page
                return render(request, 'todo/signupuser.html', {'form':RegisterForm(), 'error':'Username is already taken - please choose something different.'})
        else:
            # passwords didnt match, display error
            return render(request, 'todo/signupuser.html', {'form':RegisterForm(), 'error':'Passwords did not match.'})

@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodo')
            # return render(request, 'todo/currenttodo.html')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error':'You have some bad data in there, try again'})

@login_required
def currenttodo(request):
    # get all the not-completed todos for current user
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodo.html', {'todos':todos})

@login_required
def completedtodo(request):
    # get all the not-completed todos for current user
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodo.html', {'todos':todos})

@login_required
def viewtodo(request, todo_pk):
    # checking primary key and user ownership validation
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        # getting and passing form information for display and edit from instance
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            # instance todo implies existing object to allow update
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo, 'error':'You have some bad data in there, try again'})

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodo')

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodo')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password didnt validate.'})
        else:
            login(request, user)
            return redirect('currenttodo')

@login_required
def logoutuser (request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')