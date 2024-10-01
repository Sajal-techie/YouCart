from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')  
        else:
            print()
            messages.error(request, f"{list(form.errors.values())[-1][0]}")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user, email,password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or Password. Please try again")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')


@login_required
def home_view(request):
    print(request.user)
    return render(request, 'home.html')
