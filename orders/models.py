from django.db import models
from django.conf import settings
from events.models import Event

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('paid',      'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    user       = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='orders')
    status     = models.CharField(max_length=10,
                                  choices=STATUS_CHOICES,
                                  default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} ({self.user.email})"


class OrderItem(models.Model):
    order    = models.ForeignKey(Order,
                                 on_delete=models.CASCADE,
                                 related_name='items')
    event    = models.ForeignKey(Event,
                                 on_delete=models.PROTECT,
                                 related_name='order_items')
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'event')

    def __str__(self):
        return f"{self.quantity}× {self.event.title}"
    
    @property
    def line_total(self):
        return self.quantity * self.event.price
