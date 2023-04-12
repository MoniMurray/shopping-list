from .models import Entry, Note
from django import forms


class AddForm(forms.ModelForm):
    """Form to add a new Item to the user's shopping list"""
    class Meta:
        model = Entry
        fields = ('item_name', 'quantity', 'star', 'category',)


class NoteForm(forms.ModelForm):
    """Form to add a Note to an item on the user's shopping list"""
    class Meta:
        model = Note
        fields = ('body',)
