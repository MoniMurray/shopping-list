from django.test import TestCase
from .models import List_Item

# Create your tests here.


class TestModelsExist(TestCase):

    def test_check_item_as_done_defaults_to_True(self):
        item_name = List_Item.objects.create(item_name='Test New Item')
        self.assertTrue(item_name.check_item_as_done)

