# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0008_alumnos_keyqr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='keyQR',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
