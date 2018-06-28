from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
   1) un director solo puede tener una escuela    !crea conflitos pues en los views uso mucho este hecho!
   2) una escuela puede tener varios directores
"""


class Colegio(models.Model):
    nombre = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50, null = True, blank = True )
    nit = models.CharField(max_length = 50)
    fecha = models.DateField(null = True, blank = True )
    observaciones = models.TextField(null = True, blank = True )
    cantidadAlumnos = models.IntegerField(null = True, blank = True )

    def __str__(self):
        return '%s'%self.nombre


class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    numDocumento = models.CharField(max_length = 30, null = True, blank = True)
    area = models.CharField(max_length = 50,null = True, blank=True)
    perfil = models.IntegerField(default = 0)
    imgUser = models.ImageField(upload_to = "imgUsers/",null = True,blank = True)
    escuela = models.ManyToManyField(Colegio,blank = True)

    def __str___(self):
        return "perfil: %s"%(self.perfil)

    class Admin:
        pass


class Alumnos(models.Model):
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50 )
    padres  = models.ManyToManyField(User)
    escuela = models.ManyToManyField(Colegio,blank = True)
    numDocumento = models.CharField(max_length = 100,null = True,blank = True)
    fechaNacimiento = models.DateField(blank = True, null = True)
    email = models.EmailField()
    activo = models.BooleanField(default = True)
    imgAlumno= models.ImageField(upload_to = 'imgAlumno',blank = True,null = True)
    keyQR = models.CharField(max_length= 128, null = True,blank = True)

    def __str__(self):
        return "%s %s"%(self.nombres,self.apellidos)


class Seleccion(models.Model):
    nombre = models.CharField(max_length = 50)
    alumnos = models.ManyToManyField(Alumnos,blank = True)
    profesor = models.ForeignKey(User)
    escuela = models.ForeignKey(Colegio)

    def __str__(self):
        return "%s"%self.nombre
