def cart_count(request):
    return {"cart_count": sum(request.session.get("cart", {}).values())}
