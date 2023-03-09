from django.test import TestCase
from .models import List_Item

# Create your tests here.


class TestList_Item(TestCase):
    def test_exists(self):
        list_item = List_Item.objects.create
