from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("event", "quantity")
    extra = 0
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display   = ("id", "user", "status", "created_at", "updated_at")
    list_filter    = ("status", "created_at", "updated_at")
    search_fields  = ("user__email", "id")
    inlines        = (OrderItemInline,)
    ordering       = ("-created_at",)

    actions = ["mark_paid", "mark_cancelled"]

    def mark_paid(self, request, queryset):
        queryset.filter(status="pending").update(status="paid")
    mark_paid.short_description = "Mark selected orders as Paid"

    def mark_cancelled(self, request, queryset):
        queryset.filter(status__in=["pending", "paid"]).update(status="cancelled")
    mark_cancelled.short_description = "Cancel selected orders"
