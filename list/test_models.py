from django.test import TestCase
from .models import Entry

# Create your tests here.


class TestModels(TestCase):

    def test_star_defaults_to_True(self):
        item = Entry.objects.create(item_name='Test Entry Item')
        self.assertTrue(item.star)

