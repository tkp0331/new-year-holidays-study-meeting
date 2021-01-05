from django.contrib import admin
from django.urls import path, include
from .views import IndexView, EntryView, FacultyListView

app_name = 'univ'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("entry", EntryView.as_view(), name='entry'),
    path('faculty', FacultyListView.as_view(), name='faculty'),
]
