# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chirp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentID', models.CharField(max_length=30)),
                ('StudentName', models.CharField(max_length=50)),
                ('JavacCall', models.CharField(max_length=100)),
                ('TimeStamp', models.DateTimeField()),
                ('JavaProgram', models.TextField()),
                ('JavaCompilerOutput', models.TextField()),
                ('NumCompiles', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChirpRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentID', models.CharField(max_length=30)),
                ('StudentName', models.CharField(max_length=50)),
                ('ClassName', models.CharField(max_length=50)),
                ('MethodName', models.CharField(max_length=50)),
                ('ObjectName', models.CharField(max_length=50)),
                ('Parameters', models.CharField(max_length=100)),
                ('Result', models.TextField()),
                ('TimeStamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
