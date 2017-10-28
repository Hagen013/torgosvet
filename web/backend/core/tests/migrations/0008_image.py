# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 14:16
from __future__ import unicode_literals

import core.db.image.image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_shop_named_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='images/no_photo.png', upload_to=core.db.image.image.UploadTo, verbose_name='Картинка')),
                ('image_name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
