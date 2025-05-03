from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Event
import datetime

class EventSmokeTests(TestCase):
    def setUp(self):
        # create one future event
        self.event = Event.objects.create(
            title="🔥 Smoke Test Event",
            description="Just a test.",
            image_url="http://example.com/img.png",
            price="9.99",
            location="Test City",
            start_datetime=timezone.now() + datetime.timedelta(days=1),
            end_datetime=timezone.now() + datetime.timedelta(days=1, hours=2),
        )

    def test_catalog_shows_event(self):
        url = reverse('events:catalog')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.event.title)

    def test_detail_shows_event(self):
        url = reverse('events:detail', args=[self.event.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.event.title)
