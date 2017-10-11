# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, related_name='profile', blank=False, null=False)
    cedula = models.IntegerField(null=True, blank=True, verbose_name='Cedula')    
    nombre = models.CharField(max_length=50, verbose_name='Nombre Completo')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    telefono =  models.IntegerField(null=True, blank=True, verbose_name='Telefono')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    estado = models.BooleanField(default=False, verbose_name='Estado')

    def __unicode__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

class Noticia(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo',null=True)
    descripcion= models.TextField()
    fecha= models.DateTimeField()
    estado = models.BooleanField(default=False, verbose_name='Estado')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

#link donde enseñan las formas en que podemos heredar de un modelo ya hecho de django

#https://es.stackoverflow.com/questions/8026/modificar-el-modelo-de-usuario-de-django
#https://miguelgomez.io/django/extender-user-django/


class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField()
    fecha= models.DateTimeField()
    estado = models.BooleanField(default=False, verbose_name='Estado')

class UsuarioActividad(models.Model):
    usuario = models.ForeignKey(Usuario,null=True)
    actividad = models.ForeignKey(Actividad,null=True)

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField()
    fecha= models.DateTimeField()
    estado = models.BooleanField(default=False, verbose_name='Estado')

class ActividadEvento(models.Model):
    actividad = models.ForeignKey(Actividad,null=True)
    evento = models.ForeignKey(Evento,null=True)

class UsuarioEvento(models.Model):
    usuario = models.ForeignKey(Usuario,null=True)
    evento = models.ForeignKey(Evento,null=True)
