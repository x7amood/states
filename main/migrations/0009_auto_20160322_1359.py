# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160322_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='latitude',
            field=models.CharField(max_length=100, null=True, blank=100),
        ),
        migrations.AlterField(
            model_name='statecapital',
            name='longitude',
            field=models.CharField(max_length=100, null=True, blank=100),
        ),
    ]
