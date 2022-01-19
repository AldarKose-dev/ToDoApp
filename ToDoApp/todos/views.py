from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/todos/list')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def list_items(request):
    context = {'todo_list': ToDo.objects.all()}
    return render(request, 'todos/todo.html', context)


def insert_items(request: HttpRequest):
    todo = ToDo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list')


def delete_item(request, todo_id):
    task_to_delete = ToDo.objects.get(id=todo_id)
    task_to_delete.delete()
    return redirect('/todos/list/')


def logout_view(request):
    logout(request)
    return redirect('/accounts')
