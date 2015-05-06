# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PencilCodeEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentID', models.CharField(max_length=30)),
                ('Assignment', models.CharField(max_length=30)),
                ('ProjectName', models.CharField(max_length=50)),
                ('TimeStamp', models.DateTimeField()),
                ('Condition', models.CharField(max_length=30)),
                ('EditorMode', models.CharField(max_length=30)),
                ('EventType', models.CharField(max_length=30)),
                ('Program', models.TextField()),
                ('FloatingBlocks', models.TextField()),
                ('ProjectHTML', models.TextField()),
                ('ProjectCSS', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
