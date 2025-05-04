from django.contrib import admin
from .models import Order, OrderItem
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("event_link", "quantity", "line_total")
    fields          = ("event_link", "quantity", "line_total")
    extra           = 0
    can_delete      = False

    def event_link(self, obj):
        url = f"/admin/events/event/{obj.event.pk}/change/"
        return format_html_join(
            "", 
            '<a href="{}">{}</a>',
            ((url, obj.event.title),)
        )
    event_link.short_description = "Event"

    def line_total(self, obj):
        return obj.quantity * obj.event.price
    line_total.short_description = "Line Total"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ("id", "user", "status", "created_at", "item_count", "total_amount")
    list_filter   = ("status", "created_at")
    search_fields = ("user__email", "id")
    inlines       = (OrderItemInline,)
    ordering      = ("-created_at",)

    def item_count(self, order):
        return order.items.count()
    item_count.short_description = "Items"

    def total_amount(self, order):
        return sum(item.quantity * item.event.price for item in order.items.all())
    total_amount.short_description = "Total ($)"

    actions = ["mark_paid", "mark_cancelled"]

    def mark_paid(self, request, queryset):
        queryset.filter(status="pending").update(status="paid")
    mark_paid.short_description = "Mark selected orders as Paid"

    def mark_cancelled(self, request, queryset):
        queryset.filter(status__in=["pending", "paid"]).update(status="cancelled")
    mark_cancelled.short_description = "Cancel selected orders"
