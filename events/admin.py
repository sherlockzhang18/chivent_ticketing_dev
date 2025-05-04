from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display   = ("title", "start_datetime", "price", "available_tickets", "location")
    search_fields  = ("title", "location")
    list_filter    = ("start_datetime",)
