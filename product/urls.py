from django.urls import path
from .views import add_product_view, edit_product_view, change_status_view, delete_product_view

urlpatterns = [
    path("add_product/", add_product_view, name="add_product"),
    path("edit_product/<int:id>/", edit_product_view, name="edit_product"),
    path("delete_product/<int:id>/", delete_product_view, name="delete_product"),
    path("change_status/<int:id>/", change_status_view, name="change_status"),
]
