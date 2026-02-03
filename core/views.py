from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.decorators.http import require_http_methods
from .forms import SignUpForm

def home(request):
    return render(request, 'home2.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    return redirect('home')
