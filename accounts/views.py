from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


@login_required(login_url='my_view')
def home(request):
    title = 'QRpasSys'
    return render(request, 'pages/home.html', {'title': title})


def my_view(request):
    title = "Don't authenticated"
    return render(request, 'pages/without_an_account_page.html', {title: title})


def login_user(request):
    title = 'Login page'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'pages/login.html', {title: title})


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    title = 'Register page'
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        else:
            print(form.errors)
        return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'title': title, 'form': form})


def success(request):
    return HttpResponse('success!')
