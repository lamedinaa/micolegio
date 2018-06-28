# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0002_seleccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seleccion',
            name='alumnos',
            field=models.ManyToManyField(to='director.Alumnos', null=True, blank=True),
        ),
    ]
