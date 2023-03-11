from django.contrib import admin
from .models import Entry, Note
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):
    list_display = ('item_name', 'category', 'quantity', 'added_on', 'star')
    list_filter = ['category',]
    search_fields = ['item_name', 'category']
    actions = ['mark_as_urgent', 'mark_as_done']

    def mark_as_urgent(self, request, queryset):
        queryset.update(star=True)

    def mark_as_done(self, request, queryset):
        queryset.update(check_item_as_done=True)


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    # where we indicated Note body field was to be TextField we want it to be
    # a summernote field
    list_filter = ('item', 'added_on')
    list_display = ('item', 'added_on')
    search_fields = ['item',]
    summernote_fields = ('body')
