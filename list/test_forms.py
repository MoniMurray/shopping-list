from django.test import TestCase
from .forms import AddForm, NoteForm

class TestAddForm(TestCase):

    def test_item_name_is_required(self):
        form = AddForm({'item_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('item_name', form.errors.keys())
        self.assertEqual(form.errors['item_name'][0], 'This field is required.')

    def test_category_field_is_required(self):
        form = AddForm({'item_name': 'Test List Items'})
        self.assertFalse(form.is_valid())


