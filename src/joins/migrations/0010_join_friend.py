# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0009_auto_20150328_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friend',
            field=models.ForeignKey(null=True, related_name='referral', to='joins.Join', blank=True),
            preserve_default=True,
        ),
    ]
