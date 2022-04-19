from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppOrg import views

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a la página del Congreso Argentino de Etnobiología </h1>')

def plantilla(request):

    lista= ['primero', 
            'segundo', 
            'tercero',]
    
    nombre='Valentina'
    
    datos={
        'nombre':nombre,
        'lista': lista,
    }
        
    #plantilla_generada = template.render(datos)
    
    #versión nueva con loader
    #template=loader.get_template("mi_plantilla.html")
    #plantilla_preparada= template.render(datos)
    #return HttpResponse (plantilla_preparada)
    
    #return HttpResponse(plantilla_generada)
    return render(request, "plantilla.html", datos)