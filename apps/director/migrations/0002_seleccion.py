# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('alumnos', models.ManyToManyField(to='director.Alumnos', blank=True)),
                ('profesor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
