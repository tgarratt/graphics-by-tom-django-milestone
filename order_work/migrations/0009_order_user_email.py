# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_work', '0008_auto_20200224_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.CharField(default='', max_length=60),
        ),
    ]
