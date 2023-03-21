from django.test import TestCase
from .models import Entry


class TestViews(TestCase):
    
    def test_get_Entry_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


