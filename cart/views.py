from django.shortcuts import redirect, render, get_object_or_404
from events.models import Event
from .cart import add_to_cart, remove_from_cart, get_cart

def add_to_cart_view(request, pk):
    add_to_cart(request.session, pk)
    return redirect("cart:detail")

def remove_from_cart_view(request, pk):
    remove_from_cart(request.session, pk)
    return redirect("cart:detail")

def cart_detail(request):
    cart = get_cart(request.session)
    items, total = [], 0
    for event_id, qty in cart.items():
        evt = get_object_or_404(Event, pk=event_id)
        subtotal = evt.price * qty
        items.append({"event": evt, "quantity": qty, "subtotal": subtotal})
        total += subtotal
    return render(request, "cart/detail.html", {"items": items, "total": total})
