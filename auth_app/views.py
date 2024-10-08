from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm
from product.models import Product
from cart.models import Cart,CartItem


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


def home_view(request):
    print(request.user)
    products = Product.objects.filter(is_active=True)
    cart_items_id = CartItem.objects.filter(cart__user = request.user).values_list('product_id', flat=True) if request.user.is_authenticated else []
    print(cart_items_id)
    context = {
        'products': products,
        'cart_product_ids': cart_items_id
    }
    return render(request, 'home.html', context)


def admin_login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_home')
        else:
            return redirect('home')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home')
            else:
                messages.error(request, "You don't have permission to access this page")
        else:
            messages.error(request, "Invald email or password")

    return render(request, "admin_login.html")


@login_required(login_url='admin_login')
def admin_home_view(request):
    if request.user.is_staff:
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'admin_home.html', context)
    messages.error(request, 'You dont have permission to access this page')
    return redirect('login')