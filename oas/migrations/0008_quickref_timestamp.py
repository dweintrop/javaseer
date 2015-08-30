# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0007_pencilcodeevent_palettevisible'),
    ]

    operations = [
        migrations.AddField(
            model_name='quickref',
            name='TimeStamp',
            field=models.DateTimeField(default=datetime.date(2015, 8, 30)),
            preserve_default=False,
        ),
    ]
