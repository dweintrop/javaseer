# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oas', '0005_auto_20150511_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickRef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentID', models.CharField(max_length=30)),
                ('Assignment', models.CharField(max_length=30)),
                ('Hostname', models.CharField(max_length=100)),
                ('Condition', models.CharField(max_length=30)),
                ('EditorMode', models.CharField(max_length=30)),
                ('Page', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
