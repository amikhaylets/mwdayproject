# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20150326_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='Default_value', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default='Default_value', max_length=120),
            preserve_default=True,
        ),
    ]
