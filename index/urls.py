from django.urls import path
from .views import index, plantilla

urlpatterns = [
    path('', index),
    path('plantilla/', plantilla, name='plantilla')
]
