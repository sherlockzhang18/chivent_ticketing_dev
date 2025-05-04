def get_cart(session):
    """Return current cart dict {event_id: qty} or {}."""
    return session.get('cart', {})

def save_cart(session, cart):
    """Save cart dict back to session and mark modified."""
    session['cart'] = cart
    session.modified = True

def add_to_cart(session, event_id, qty=1):
    """Add qty of event_id to cart."""
    cart = get_cart(session)
    cart[str(event_id)] = cart.get(str(event_id), 0) + qty
    save_cart(session, cart)

def remove_from_cart(session, event_id):
    """Remove an event entirely from cart."""
    cart = get_cart(session)
    cart.pop(str(event_id), None)
    save_cart(session, cart)

def clear_cart(session):
    """Empty the cart."""
    save_cart(session, {})
