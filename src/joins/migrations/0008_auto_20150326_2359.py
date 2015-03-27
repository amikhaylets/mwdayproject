# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_auto_20150326_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(unique=True, default='Default_value', max_length=120),
            preserve_default=True,
        ),
    ]
