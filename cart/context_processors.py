from cart.models import CartItem
from auth_app.models import CustomUser


def cart_count(request):
    context = {}
    if request.user.is_authenticated:
        count = CartItem.objects.filter(cart__user=request.user).count()
        context['cart_count'] = count
    
    return context