# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='testoffer',
            name='old_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Старая цена'),
        ),
        migrations.AddField(
            model_name='testofferpage',
            name='old_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Старая цена'),
        ),
    ]
