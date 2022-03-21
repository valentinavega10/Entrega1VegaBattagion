from django.urls import path
from .views  import nuevo_congreso

urlpatterns = [
    path('nuevo/', nuevo_congreso , name='nuevo_congreso')
]