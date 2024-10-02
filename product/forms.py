from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("The price must be a positive value.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise ValidationError("Stock cannot be negative.")
        return stock

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Only PNG, JPG, and JPEG formats are allowed.")

            max_size = 5 * 1024 * 1024 
            if image.size > max_size:
                raise ValidationError("Image size should not exceed 5MB.")
        return image