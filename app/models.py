# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', blank=False, null=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre Completo')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    telefono =  models.IntegerField(null=True, blank=True, verbose_name='Telefono')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')

    def __unicode__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

class Noticia(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre')
    titulo = models.CharField(max_length=50, verbose_name='Titulo',null=True)
    estado = models.BooleanField(default=False, verbose_name='Estado')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

class Activity(models.Model):
    nombre = models.CharField(max_length=50)

class UserActivity(models.Model):
    user = models.ForeignKey(UserProfile,null=True)
    activity = models.ForeignKey(Activity,null=True)


