# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0003_remove_register_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='log_out',
            field=models.DateTimeField(null=True, verbose_name='Log out'),
        ),
    ]
