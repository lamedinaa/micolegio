# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_auto_20180623_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seleccion',
            name='alumnos',
            field=models.ManyToManyField(to='director.Alumnos', blank=True),
        ),
    ]
