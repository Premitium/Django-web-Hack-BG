# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_offer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'PENDING'), (2, 'APPROVED'), (3, 'REJECTED')], default=1),
        ),
    ]