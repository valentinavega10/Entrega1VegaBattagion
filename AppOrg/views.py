from django.http import HttpResponse
from django.shortcuts import render
from AppOrg.models import Congreso
# Create your views here.

def nuevo_congreso(request):
    
    nuevo_congreso = Congreso(nombre='Botánica Argentina', numero='2')
    nuevo_congreso.save()
    return HttpResponse(f"Se creó el congreso {nuevo_congreso.nombre} número {nuevo_congreso.numero}")