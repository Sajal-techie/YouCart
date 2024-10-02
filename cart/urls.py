from django.urls import path
from .views import cart_view, add_to_cart_view, remove_from_cart_view, increase_quantity_view, decrease_quantity_view, create_order, order_history


urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add_cart/<int:id>/', add_to_cart_view, name='add_cart'),
    path('remove_cart/<int:id>/', remove_from_cart_view, name='remove_cart'),
    path('increase_quantity/<int:id>/', increase_quantity_view, name='increase_quantity'),
    path('decrease_quantity/<int:id>/', decrease_quantity_view, name='decrease_quantity'),
    path('place_order/', create_order, name='place_order'),
    path('order_history/', order_history, name="order_history"),
]
