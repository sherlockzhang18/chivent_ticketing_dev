"""chivent_project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Built-in admin site at /admin/
    path('admin/',    admin.site.urls),
    path("orders/",   include("orders.urls")),
    path('cart/',     include('cart.urls',    namespace='cart')),
    path("accounts/", include("accounts.urls")),
    # The root URL
    path('',          include('events.urls',  namespace='events')),
]



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)