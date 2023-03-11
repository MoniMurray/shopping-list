from django.shortcuts import render
from django.views import generic
from .models import Entry


# Create your views here.
class EntryList(generic.ListView):

    model = Entry
    queryset = Entry.objects.all()
    template_name = 'index.html'
