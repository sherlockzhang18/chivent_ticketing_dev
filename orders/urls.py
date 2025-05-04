from django.urls import path
from .views import checkout_view, payment_view

app_name = "orders"

urlpatterns = [
    path("checkout/", checkout_view, name="checkout"),
    path("payment/<int:order_id>/", payment_view, name="payment"),
]
