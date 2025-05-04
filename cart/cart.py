# helper functions for cart management

def get_cart(session):
    return session.get("cart", {})

def save_cart(session, cart):
    session["cart"] = cart
    session.modified = True

def add_to_cart(session, event_id, qty=1):
    cart = get_cart(session)
    cart[str(event_id)] = cart.get(str(event_id), 0) + qty
    save_cart(session, cart)

def remove_from_cart(session, event_id):
    cart = get_cart(session)
    cart.pop(str(event_id), None)
    save_cart(session, cart)
