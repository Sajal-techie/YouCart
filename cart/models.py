from django.db import models
from auth_app.models import CustomUser
from product.models import Product


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, related_name="cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"
    
    @property
    def total_price(self):
        cart_items = self.cart_item.all()
        total = sum([item.total_price for item in cart_items])
        return total 


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.name} x {self.quantity}"
    
    @property
    def total_price(self):
        return self.product.price * self.quantity
    

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="ordered")
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}'s Order {self.id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    

    def __str__(self):
        return f"{self.product.name} x {self.quantity} item"
    