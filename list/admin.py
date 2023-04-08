from django.contrib import admin
from .models import Entry, Note
from django_summernote.admin import SummernoteModelAdmin


class EntryNoteInline(admin.TabularInline):
    """Create an additional table into which admin can add a note"""
    model = Note
    readonly_fields = ['id', 'added_on']


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):
    """Create an Entry model view for admin to control and view
    all actions enabled within this model"""

    list_display = (
        'item_name',
        'category',
        'quantity',
        'added_on',
        'star',
        'check_item_as_done')
    # add the additional table to the Entry model table in admin's view
    inlines = [EntryNoteInline, ]
    list_filter = ['category', ]
    search_fields = ['item_name', 'category']
    actions = ['mark_as_urgent', 'mark_as_done']

    # toggle star On/Off
    def mark_as_urgent(self, request, queryset):
        queryset.update(star=True)

    # toggle checkbox On/Off
    def mark_as_done(self, request, queryset):
        queryset.update(check_item_as_done=True)


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    """Create a Note model view for admin to control and view
    all actions enabled within this model"""

    # where we indicated Note body field was to be TextField we want it to be
    # a summernote field
    list_filter = ('item', 'added_on')
    list_display = ('item', 'added_on')
    search_fields = ['item', ]
    summernote_fields = ('body')
