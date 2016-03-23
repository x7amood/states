# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160314_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCapital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=100)),
                ('longitude', models.FloatField(null=True, blank=100)),
                ('capital_population', models.IntegerField(null=True, blank=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital_population',
        ),
        migrations.RemoveField(
            model_name='state',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='longitude',
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='main.State'),
        ),
    ]
