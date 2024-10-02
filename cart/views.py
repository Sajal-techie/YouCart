from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Cart, CartItem, Order, OrderItem
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
        if product.stock == 0:
            messages.error(request, f"{product.name} - Out of stock")
            return redirect('home')
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
    

@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(cart__user=request.user).prefetch_related('product')

    if not cart_items.exists():
        messages.error(request, "Your cart is empty")
        return redirect('cart')
    for item in cart_items:
        if item.product.stock < item.quantity:
            messages.error(request, f"{item.product.name} - Out of Stock")
            return redirect('cart')
        elif item.quantity <= 0:
            messages.error(request, "Quantity must be Greater than 0")
            return redirect('cart')
    total_amount = sum(item.total_price for item in cart_items)
    with transaction.atomic():
        order = Order.objects.create(
            user = request.user,
            total_amount = total_amount,
        )
        for item in cart_items:
            obj = OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity
            )
            obj.product.stock -= obj.quantity
            obj.product.save()

        cart_items.delete()

    messages.success(request, "Your Order has been placed Successfully")
    return redirect('cart')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    return render(request, "orders.html", {'orders':orders})