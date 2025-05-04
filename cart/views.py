from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from events.models import Event
from .cart import add_to_cart, remove_from_cart, get_cart


def add_to_cart_view(request, pk):
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)

        # parse requested qty
        try:
            qty = int(request.POST.get("quantity", 1))
            qty = max(qty, 1)
        except (ValueError, TypeError):
            qty = 1

        # **use the DB count directly**
        available = event.available_tickets

        if available <= 0:
            messages.error(request, "Sorry, this event is sold out.")
            return redirect("events:detail", pk=pk)

        if qty > available:
            messages.error(
                request,
                f"Only {available} ticket{'s' if available>1 else ''} remaining — you tried to add {qty}."
            )
            return redirect("events:detail", pk=pk)

        # Deduct from MySQL
        event.available_tickets -= qty
        event.save()

        # Now put into the session cart
        add_to_cart(request.session, pk, qty)

    # Send them back to the event detail page
    return redirect("events:detail", pk=pk)


def remove_from_cart_view(request, pk):
    cart = get_cart(request.session)
    qty = cart.get(str(pk), 0)
    if qty > 0:
        event = get_object_or_404(Event, pk=pk)
        # refund them
        event.available_tickets += qty
        event.save()
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
