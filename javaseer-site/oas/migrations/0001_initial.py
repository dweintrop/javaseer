# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Javaseer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentID', models.CharField(max_length=30)),
                ('StudentName', models.CharField(max_length=50)),
                ('JavacCall', models.CharField(max_length=100)),
                ('TimeStamp', models.DateTimeField()),
                ('JavaProgram', models.TextField()),
                ('JavaCompilerOutput', models.TextField()),
                ('NumRuns', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
