import django_filters
from .models import Entry
from django_filters import CharFilter


class EntryFilter(django_filters.FilterSet):
    entry = CharFilter(field_name='item_name', lookup_expr='icontains')

    class Meta:
        model = Entry
        fields = ['item_name', 'category']
