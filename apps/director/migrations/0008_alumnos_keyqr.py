# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0007_seleccion_escuela'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='keyQR',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
