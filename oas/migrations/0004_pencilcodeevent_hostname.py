# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='pencilcodeevent',
            name='Hostname',
            field=models.CharField(default='pre-hostname', max_length=30),
            preserve_default=False,
        ),
    ]
