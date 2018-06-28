# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0006_remove_seleccion_escuela'),
    ]

    operations = [
        migrations.AddField(
            model_name='seleccion',
            name='escuela',
            field=models.ForeignKey(default=1, to='director.Colegio'),
            preserve_default=False,
        ),
    ]
