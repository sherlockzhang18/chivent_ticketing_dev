"""chivent_project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


# chivent_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',      include('events.urls',  namespace='events')),
    # path('cart/', include('cart.urls',    namespace='cart')),
]



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)