from django.urls import path
from .views import checkout_view, payment_view, my_orders, my_order_detail

app_name = "orders"

urlpatterns = [
    path("checkout/", checkout_view, name="checkout"),
    path("payment/<int:order_id>/", payment_view, name="payment"),
    path("my/", my_orders, name="my_orders"),
    path("my/<int:order_id>/", my_order_detail, name="my_order_detail"),
]
