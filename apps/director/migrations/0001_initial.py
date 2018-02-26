# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('numDocumento', models.CharField(max_length=100, null=True, blank=True)),
                ('fechaNacimiento', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('activo', models.BooleanField(default=True)),
                ('imgAlumno', models.ImageField(null=True, upload_to=b'imgAlumno', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('nit', models.CharField(max_length=50)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('cantidadAlumnos', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numDocumento', models.CharField(max_length=30, null=True, blank=True)),
                ('area', models.CharField(max_length=50, null=True, blank=True)),
                ('perfil', models.IntegerField(default=0)),
                ('imgUser', models.ImageField(null=True, upload_to=b'imgUsers/', blank=True)),
                ('escuela', models.ManyToManyField(to='director.Colegio', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='alumnos',
            name='escuela',
            field=models.ManyToManyField(to='director.Colegio', blank=True),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='padres',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
