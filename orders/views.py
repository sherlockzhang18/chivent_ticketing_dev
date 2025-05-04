from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from cart.cart import get_cart, clear_cart
from .models import Order, OrderItem
from events.models import Event

@login_required
def checkout_view(request):
    if request.method != "POST":
        return redirect("cart:detail")

    cart = get_cart(request.session)
    if not cart:
        messages.info(request, "Your cart is empty.")
        return redirect("events:catalog")

    # 1) Inventory check
    insufficient = []
    for event_id, qty in cart.items():
        event = get_object_or_404(Event, pk=event_id)
        if event.available_tickets < qty:
            insufficient.append((event, event.available_tickets))
    if insufficient:
        for event, avail in insufficient:
            messages.error(
                request,
                f"Not enough tickets for “{event.title}”: only {avail} left."
            )
        return redirect("cart:detail")

    # 2) Create Order & OrderItems, decrement inventory
    order = Order.objects.create(user=request.user, status="pending")
    for event_id, qty in cart.items():
        event = get_object_or_404(Event, pk=event_id)
        OrderItem.objects.create(order=order, event=event, quantity=qty)
        event.available_tickets -= qty
        event.save()

    # 3) Clear session cart
    clear_cart(request.session)

    # 4) Show checkout confirmation
    return render(request, "orders/checkout_success.html", {"order": order})


@login_required
def payment_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    total = sum(item.quantity * item.event.price for item in order.items.all())

    if request.method == "POST":
        order.status  = "paid"
        order.paid_at = timezone.now()
        order.save()
        messages.success(request, f"Payment received for Order #{order.id}")
        return render(request, "orders/payment_success.html", {"order": order})

    return render(request, "orders/payment.html", {"order": order, "total": total})
