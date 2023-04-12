from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import (
    FormView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponseRedirect
from .models import Entry, Note
from .forms import AddForm, NoteForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


CATEGORY_CHOICES = [
    ('a', 'Fresh'),
    ('b', 'Dairy'),
    ('c', 'Frozen'),
    ('d', 'Bakery'),
    ('e', 'Dry Ingredients'),
    ('f', 'Household'),
    ('g', 'Pet'),
    ('h', 'Personal Care'),
    ('i', 'Treats'),
    ('j', 'Alcohol')
]


@login_required(login_url='/account/login.html')
def get_context_data(self, **kwargs):
    profile = Profile.objects.get(user=self.kwargs['pk'])
    context = {
        'profile': profile,
        'form': ProfileForm(instance=profile)
    }
    return context


class EntryList(LoginRequiredMixin, generic.ListView):
    """A logged in User will be able to view their entire
    shopping list in the Home page, and have access to all the features
    of the list ie. CRUD, Search and Adding Notes"""

    model = Entry
    template_name = 'index.html'
    paginate_by = 100

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_queryset(self, **kwargs):
        queryset = Entry.objects.filter(user=self.request.user)
        search = self.request.GET.get('query')
        
        if search:
            queryset = queryset.filter(
                Q(category__icontains=search) |
                Q(item_name__icontains=search) |
                Q(category__in=[
                    choice[0] for choice in CATEGORY_CHOICES if
                    choice[1].lower().startswith(search.lower())])

            )
        return queryset


class AddView(FormView):
    """Create a new shopping list entry using the fields from Entry model"""

    template_name = 'add_to_list.html'
    form_class = AddForm
    success_url = reverse_lazy('home')

    # ensure new items are automatically saved to the logged in user
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(id=self.request.user.id)
        messages.success(self.request, 'Added successfully.')
        form.save()
        return super().form_valid(form)


class EditView(UserPassesTestMixin, UpdateView):
    """Edit shopping list entry using the entry's primary key"""

    model = Entry
    template_name = 'edit_entry.html'
    form_class = AddForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')

    # extra security - only permit edit if logged-in user created item
    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        messages.success(self.request, 'Edited successfully.')
        instance = form.save()
        return super(EditView, self).form_valid(form)


def add_note(request, item_id):
    # get an instance of the shopping list item with an id equal to the
    # one that was clicked in the index.html template but
    # call the note.html template having populated it with the shopping
    # list item name and add our note to the body field, return to 'Home'

    entry = get_object_or_404(Entry, id=item_id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                entry = Entry.objects.get(id=item_id)
            except Entry.DoesNotExist:
                pass
            instance.item = entry
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        form = NoteForm()
    context = {
        'entry': entry,
        'form': form
    }
    return render(request, 'note.html', context)


class Delete(UserPassesTestMixin, DeleteView):
    """Target the entry with the pk again to Delete Item"""

    model = Entry
    pk_url_kwarg = 'pk'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deleted successfully."

    # extra security - only permit delete if logged-in user created item
    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        instance = form.save()
        return super(Delete, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Delete, self).delete(request, *args, **kwargs)


def toggle_star(request, item_id):
    # toggle the star state to On/Off

    item = get_object_or_404(Entry, id=item_id)
    item.star = not item.star
    item.save()
    return redirect('home')


def toggle_check(request, item_id):
    # toggle the checkbox state to On/Off

    item = get_object_or_404(Entry, id=item_id)
    item.check_item_as_done = not item.check_item_as_done
    item.save()
    return redirect('home')
