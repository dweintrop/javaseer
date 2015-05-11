# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0002_pencilcodeevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentID', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=100)),
                ('School', models.CharField(max_length=30)),
                ('Class', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Condition', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
