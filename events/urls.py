from django.urls import path
from .views import CatalogView, EventDetailView

app_name = 'events'

urlpatterns = [
    path('',            CatalogView.as_view(),    name='catalog'),
    path('e/<int:pk>/', EventDetailView.as_view(), name='detail'),
]
