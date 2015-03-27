# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20150326_2331'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
