from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import NoteForm
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
class EntryList(generic.ListView):

    model = Entry
    queryset = Entry.objects.all()
    template_name = 'index.html'
    paginate_by = 25


class AddView(CreateView):
    # CRUD - Create a new shopping list entry using the fields from Entry model

    model = Entry
    template_name = 'add_to_list.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    # Next, add a success flash message when form is submitted.
    # # should I be able to add a post method to this class-based view?

    # messages.add_message(request, messages.INFO, 'Hello world.')
    # Not working - first 'request' is an error,
    # # def post(self, request, *args, **kwargs):
    #     form = AddForm(data=request.POST)
    #     if form.is_valid():
    #         messages.success(request, 'Added successfully.')
    #         else:
    #  form = AddForm()
    #         return HttpResponseRedirect('/success/')

    #     return render(request, 'add_to_list.html', {'form': AddForm})


class EditView(UpdateView):
    # CRUD - Edit shopping list entry using the entry's primary key

    model = Entry
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


def toggle_star(request, item_id):
    # toggle the star state to solid/empty
    # print("function called")
    item = get_object_or_404(Entry, id=item_id)
    item.star = not item.star
    item.save()
    return redirect('home')


def toggle_check(request, item_id):
    # toggle the checkbox state to solid/empty
    # print("function called")
    item = get_object_or_404(Entry, id=item_id)
    item.check_item_as_done = not item.check_item_as_done
    item.save()
    return redirect('home')
