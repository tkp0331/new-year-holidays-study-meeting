from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('bar', views.BarView.as_view()),
    path('wave', views.WaveView.as_view()),
    path('table', views.TableView.as_view()),
]
