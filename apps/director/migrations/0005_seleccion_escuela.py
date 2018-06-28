# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0004_auto_20180623_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='seleccion',
            name='escuela',
            field=models.ForeignKey(default=2, to='director.Colegio'),
            preserve_default=False,
        ),
    ]
