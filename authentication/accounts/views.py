from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login
            return redirect('authentication:hello')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login
            return redirect('hello')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})