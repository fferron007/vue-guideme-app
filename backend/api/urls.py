from django.urls import path
from .views import filters, merchants

urlpatterns = [
    path('filters/', filters, name='filters'),
    path('merchants/', merchants, name='merchants'),
]
