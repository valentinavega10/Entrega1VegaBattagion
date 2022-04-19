from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppOrg.models import Congreso
from AppOrg import views
# Create your views here.

def nuevo_congreso(request):
    
    nuevo_congreso = Congreso(nombre='Botánica Argentina', numero='2')
    nuevo_congreso.save()
    return HttpResponse(f"Se creó el congreso {nuevo_congreso.nombre} número {nuevo_congreso.numero}")

def inicio(request):
    
    return render(request, "AppOrg/inicio.html")

def congresos (request):
    
    return render(request, "AppOrg/congresos.html")

def expositores (request):
    
    return render(request, "AppOrg/expositores.html")

def oyentes (request):
    
    return render(request, "AppOrg/oyentes.html")

def simposios (request):
    
    return render(request, "AppOrg/simposios.html")