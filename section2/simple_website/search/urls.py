from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('drive', views.DriveView.as_view()),
    path('set', views.SetView.as_view()),
]