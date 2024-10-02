from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from product.models import Product


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    context = {
        'cart_items':cart_items,
        'total_amount': cart.total_price
    }
    return render(request, 'cart.html', context)


@login_required
def add_to_cart_view(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, f"{cart_item.product.name} added to cart")
        return redirect('cart')
    except Exception as e:
        messages.error(request, "Product not found")
        return redirect('cart')
    

@login_required
def remove_from_cart_view(request, id):
    try:
        cart_item = get_object_or_404(CartItem, id=id, cart__user=request.user)
        cart_item.delete()
        messages.warning(request, f"{cart_item.product.name} removed from cart")
        return redirect('cart')
    except Exception as e:
        messages.error(request, "Item not found")
        return redirect('cart')


@login_required
def increase_quantity_view(request, id):
    try:
        cart_item = get_object_or_404(CartItem, id=id, cart__user=request.user)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f"Quantity increased successfully")
        else:
            messages.error(request, 'Max stock limit reached')
        return redirect('cart')
    except Exception as e:
        messages.error(request, "Item not found")
        return redirect('cart')


@login_required
def decrease_quantity_view(request, id):
    try:
        cart_item = get_object_or_404(CartItem, id=id, cart__user=request.user)
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, "Quantity decreased succesfully")
        else:
            messages.error(request, "Quantity must be greate than zero")
        return redirect('cart') 
    except Exception as e:
        messages.error(request, "Item not found")
        return redirect('cart')