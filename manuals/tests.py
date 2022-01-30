from django.test import TestCase
from django.urls import reverse


class ManualsTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('manuals:index'))
        self.assertEqual(response.status_code, 200)
