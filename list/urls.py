from . import views
from django.urls import path

# add url paths for views

urlpatterns = [
    path('', views.EntryList.as_view(), name='home'),
    path('add/', views.AddView.as_view(), name='add'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('note/<item_id>/', views.add_note, name='note'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('home/star/<item_id>', views.toggle_star, name='toggle_star'),
    path('home/check/<item_id>', views.toggle_check, name='toggle_check'),
]
