from django.views.generic import ListView, DetailView
from .models import Event

class CatalogView(ListView):
    model = Event
    template_name = 'events/catalog.html'
    context_object_name = 'events'
    paginate_by = 12  # option: split into pages

    def get_queryset(self):
        # only future events
        from django.utils import timezone
        return Event.objects.filter(start_datetime__gte=timezone.now())

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
