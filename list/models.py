from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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


QUANTITY_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]

# Create your models here.


class Entry(models.Model):

    # set attributes for List items Table
    item_name = models.CharField(
        max_length=60, null=False, blank=False, unique=True)
    quantity = models.IntegerField(choices=QUANTITY_CHOICES, default='1')
    star = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Fresh')
    added_on = models.DateTimeField(auto_now_add=True)
    check_item_as_done = models.BooleanField(default=False)

    # helper methods
    class Meta:
        ordering = ['-added_on', '-star',]

    def __str__(self):
        return self.item_name


class Note(models.Model):

    # set attributes for Notes Table

    item = models.OneToOneField(
        Entry, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    # helper method

    def __str__(self):
        return self.body
