from . import views
from django.urls import path

urlpatterns = [
    path('', views.EntryList.as_view(), name='home'),
    path('add/', views.AddView.as_view(), name='add'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]
