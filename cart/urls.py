from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="detail"),
    path("add/<int:pk>/", views.add_to_cart_view, name="add"),
    path("remove/<int:pk>/", views.remove_from_cart_view, name="remove"),
]
