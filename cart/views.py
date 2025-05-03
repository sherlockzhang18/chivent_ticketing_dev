# from django.shortcuts import redirect, render
# from django.views.generic import TemplateView
# from .utils import get_cart, add_item, remove_item

# class CartView(TemplateView):
#     template_name = 'cart/cart.html'

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         cart = get_cart(self.request)
#         # build items list here...
#         ctx['cart'] = cart
#         return ctx

# def add_to_cart(request):
#     if request.method == 'POST':
#         event_id = request.POST.get('event_id')
#         add_item(request, event_id)
#     return redirect('cart')

# def remove_from_cart(request):
#     if request.method == 'POST':
#         event_id = request.POST.get('event_id')
#         remove_item(request, event_id)
#     return redirect('cart')
