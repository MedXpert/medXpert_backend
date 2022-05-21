from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


# Create your views here.
def signup_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:api')
        else:
            messages.info(request, 'Username or Password is incorrect!')
            return render(request, 'accounts/login.html')
    context = {}
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authentication:api')