from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product


def add_product_view(request):
    if request.method == 'POST':
        print(request.FILES)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
        else:
            print(form.errors)
    return redirect('admin_home')
 
#  add success and error messages
def edit_product_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
        else:
            print(form.errors)
    return redirect('admin_home')


def change_status_view(request, id):
    product = get_object_or_404(Product, id=id)
    if product.is_active:
        product.is_active = False
    else:
        product.is_active = True
    product.save()
    return redirect('admin_home')


def delete_product_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()

    return redirect('admin_home')