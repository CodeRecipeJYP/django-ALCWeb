# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170213_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=b' '),
        ),
    ]
