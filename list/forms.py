from .models import Entry, Note
from django import forms


class AddForm(forms.ModelForm):
    class Meta:
        model = Entry 
        # fields = '__all__'
        fields = ('item_name', 'quantity', 'star', 'category',)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note 
        fields = ('item', 'body',)
