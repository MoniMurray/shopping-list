from . import views
from django.urls import path

urlpatterns = [
    path('', views.EntryList.as_view(), name='home'),
    path('add/', views.AddView.as_view(), name='add'),
]
