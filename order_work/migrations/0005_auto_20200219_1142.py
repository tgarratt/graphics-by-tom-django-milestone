# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-19 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_work', '0004_order_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='draft',
            field=models.ImageField(blank=True, null=True, upload_to='media/draft'),
        ),
    ]
