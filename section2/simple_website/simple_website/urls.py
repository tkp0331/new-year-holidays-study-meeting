from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('math/', include('maths.urls')),
    path('search/', include('search.urls')),
]
