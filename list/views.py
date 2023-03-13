from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Entry
from .forms import NoteForm
from django.urls import reverse_lazy


# Create your views here.
class EntryList(generic.ListView):

    model = Entry
    queryset = Entry.objects.all()
    template_name = 'index.html'
    paginate_by = 3

    # def get_shopping_list(request):
    #     entries = Entry.objects.all()
    #     context = {
    #         'entries': entries
    #     }

    #     return render(request, 'shopping-list/templates/index.html', context)

class AddView(CreateView):
    # CRUD - Create a new shopping list entry using the fields from Entry model
    
    model = Entry
    # fields = []
    template_name = 'add_to_list.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

