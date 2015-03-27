# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0006_auto_20150326_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(max_length=120, default='Default_value'),
            preserve_default=True,
        ),
    ]
