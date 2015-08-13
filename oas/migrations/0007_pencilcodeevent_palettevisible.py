# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0006_quickref'),
    ]

    operations = [
        migrations.AddField(
            model_name='pencilcodeevent',
            name='PaletteVisible',
            field=models.CharField(default='see_editor_mode', max_length=30),
            preserve_default=False,
        ),
    ]
