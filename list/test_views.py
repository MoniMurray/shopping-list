from django.test import TestCase
from .models import Entry
from django.urls import reverse, reverse_lazy


class TestViews(TestCase):

    def test_get_Entry_list(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_add_to_list_page(self):
        response = self.client.get('/add', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_to_list.html')

