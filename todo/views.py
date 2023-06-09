from django.shortcuts import render, redirect
from django.views import View
from django.http.response import Http404
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TODOForm
from .models import ToDo





class ToDoHome(LoginRequiredMixin, View):
    login_url = "login/"

    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_authenticated:
            form = TODOForm()
            todos = ToDo.objects.filter(user=request.user).order_by("priority")
            return render(request, "todo/todo.html", {
                "form": form,
                "todos": todos,
            })
    
    def post(self, request):
        if request.user.is_authenticated:
            form = TODOForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                todo.save()
                return redirect("todo-home")
            else:
                return render(request, "todo/todo.html", {
                    "form": form,
                })

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "todo/login.html", {
            "form": form,
        })
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("todo-home")
        else:
            return render(request, "todo/login.html", {
                "form": form,
            })


class LogoutView(LoginRequiredMixin, View):
    login_url = "login/"
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect("log-in")


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "todo/signup.html", {
            "form": form,
        })
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log-in")
        else:
            return render(request, "todo/signup.html", {
                "form": form,
            })
        

def remove_todo(request, pk):
    if request.method == "GET":
        todo = ToDo.objects.get(pk=pk, user=request.user)
        todo.delete()
        return redirect("todo-home")
    

def change_todo_status(request, pk, status):
    if request.method == "GET":
        todo = ToDo.objects.get(user=request.user, pk=pk)
        todo.status = status
        todo.save()
        return redirect("todo-home")

        
