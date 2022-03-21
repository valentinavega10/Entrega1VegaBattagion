from django.db import models

# Create your models here.
class Congreso(models.Model):
    
    nombre=models.CharField(max_length=50)
    numero=models.IntegerField()

class Oyente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.IntegerField()

class Expositor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.IntegerField()
    profesión = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    
class Simposio(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()
    presente= models.BooleanField()
    