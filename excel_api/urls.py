from django.urls import path
from . import views

urlpatterns = [
    path('read-excel/', views.read_excel, name='read_excel'),
]
