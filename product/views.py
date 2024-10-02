from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductForm
from .models import Product


def add_product_view(request):
    if request.method == 'POST':
        print(request.FILES)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product added successfully")
            return redirect('admin_home')
        else:
            print(form.errors)
            messages.error(request, f"{list(form.errors.values())[-1][0]}")
    return redirect('admin_home')


def edit_product_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated Successfully")
            return redirect('admin_home')
        else:
            print(form.errors)
            messages.error(request, f"{list(form.errors.values())[-1][0]}")
    return redirect('admin_home')


def change_status_view(request, id):
    product = get_object_or_404(Product, id=id)
    if product.is_active:
        product.is_active = False
    else:
        product.is_active = True
    product.save()
    messages.success(request, f"Product {"listed" if product.is_active else "unlisted" } successfully")
    return redirect('admin_home')


def delete_product_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        messages.success(request, f"{product.name} - deleted Successfully")
    return redirect('admin_home')