# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unpurchasable_form', '0002_auto_20200219_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_piece',
            name='piece',
            field=models.ImageField(blank=True, null=True, upload_to='media/piece_img'),
        ),
    ]
