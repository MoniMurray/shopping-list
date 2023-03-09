from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


CATEGORY_CHOICES = [
    ('1', 'Fresh'),
    ('2', 'Dairy'),
    ('3', 'Frozen'),
    ('4', 'Bakery'),
    ('5', 'Dry Ingredients'),
    ('6', 'Household'),
    ('7', 'Pet'),
    ('8', 'Personal Care'),
    ('9', 'Treats'),
    ('10', 'Alcohol')
]


QUANTITY_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')

]

# Create your models here.


class List_Item(models.Model):

    # set attributes for List items Table
    item_name = models.CharField(
        max_length=60, null=False, blank=False, unique=True)
    quantity = models.IntegerField(choices=QUANTITY_CHOICES, default=1)
    star = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)
    check_item_as_done = models.BooleanField(default=False)

    # helper methods
    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.item_name


class Notes(models.Model):

    # set attributes for Notes Table

    item = models.OneToOneField(List_Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    # helper method

    def __str__(self):
        return self.body
