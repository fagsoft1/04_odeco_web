# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0011_cacheconfiguration_tiempo_cache_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='cacheconfiguration',
            name='tiempo_cache_clientes',
            field=models.PositiveIntegerField(default=86400, verbose_name='Clientes Tiempo Cache'),
        ),
    ]
