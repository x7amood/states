# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160310_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='latitide',
            new_name='latitude',
        ),
    ]
