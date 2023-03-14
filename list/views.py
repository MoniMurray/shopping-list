from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Entry
from .forms import NoteForm
from django.urls import reverse_lazy
from django.contrib import messages


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

    # Next, add a success flash message when form is submitted.  
    # should I be able to add a post method to this class-based view?

    # messages.add_message(request, messages.INFO, 'Hello world.')
    # 
    # Not working - first 'request' is an error, 
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         messages.add_message(messages.INFO, 'Hello world.')
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'form': form})
    


class EditView(UpdateView):
    # CRUD - Edit shopping list entry using the entry's primary key

    model = Entry
    # fields = []
    template_name = 'edit_entry.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')


class Delete(DeleteView):
    # CRUD - Target the entry with the pk again

    model = Entry
    pk_url_kwarg = 'pk'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

