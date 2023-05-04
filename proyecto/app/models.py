from django.db import models

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()

class Gato(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    edad = models.IntegerField()

class Pajaro(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    peso = models.IntegerField()