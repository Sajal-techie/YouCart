from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images')
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name},  {self.price},  {self.stock}"
