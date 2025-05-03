from django.urls import path
from .views import CartView, add_to_cart, remove_from_cart

urlpatterns = [
    # Cart summary: http://localhost:8000/cart/
    path('', CartView.as_view(), name='cart'),
    # Add/remove (POST targets)
    path('add/',    add_to_cart,    name='cart-add'),
    path('remove/', remove_from_cart, name='cart-remove'),
]