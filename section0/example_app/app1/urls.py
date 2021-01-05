from django.urls import path

from .views import Hello, World

urlpatterns = [
    path('hello', Hello.as_view()),
    path('world', World.as_view()),
]
