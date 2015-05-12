# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0004_pencilcodeevent_hostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pencilcodeevent',
            name='Hostname',
            field=models.CharField(max_length=100),
        ),
    ]
