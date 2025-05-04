from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from events.models import Event
from .cart import add_to_cart, remove_from_cart, get_cart

@login_required
def add_to_cart_view(request, pk):
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)
        # parse quantity
        try:
            qty = int(request.POST.get("quantity", 1))
            qty = max(qty, 1)
        except (ValueError, TypeError):
            qty = 1

        # only check DB availability, do NOT adjust it here
        if event.available_tickets < qty:
            messages.error(
                request,
                f"Only {event.available_tickets} ticket{'s' if event.available_tickets!=1 else ''} remaining."
            )
            return redirect("events:detail", pk=pk)

        add_to_cart(request.session, pk, qty)

    return redirect("events:detail", pk=pk)


@login_required
def remove_from_cart_view(request, pk):
    # simply remove from session—no inventory return
    remove_from_cart(request.session, pk)
    return redirect("cart:detail")


@login_required
def cart_detail(request):
    cart = get_cart(request.session)
    items, total = [], 0
    for event_id, qty in cart.items():
        evt = get_object_or_404(Event, pk=event_id)
        subtotal = evt.price * qty
        items.append({"event": evt, "quantity": qty, "subtotal": subtotal})
        total += subtotal
    return render(request, "cart/detail.html", {"items": items, "total": total})
