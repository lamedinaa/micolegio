# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0005_seleccion_escuela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seleccion',
            name='escuela',
        ),
    ]
