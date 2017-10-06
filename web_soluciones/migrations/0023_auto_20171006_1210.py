# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 17:10
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0022_solucion_boton_soluciones_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='solucion',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='solucion',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
