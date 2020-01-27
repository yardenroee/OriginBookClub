from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you may now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'profile.html')
