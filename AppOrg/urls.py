from django.urls import path
from AppOrg import views
from .views  import nuevo_congreso

urlpatterns = [
    path('', nuevo_congreso , name='nuevo_congreso'),
    
    
]