from django.db import models

class Event(models.Model):
    title          = models.CharField(max_length=200)
    description    = models.TextField()
    image          = models.ImageField(
                       upload_to='event_images/',
                       blank=True,
                       null=True,
                       help_text="Upload a poster/photo for this event"
                       )
    price          = models.DecimalField(max_digits=7, decimal_places=2)
    location       = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime   = models.DateTimeField()
    available_tickets = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['start_datetime']

    def __str__(self):
        return f"{self.title} @ {self.start_datetime:%Y-%m-%d %H:%M}"
