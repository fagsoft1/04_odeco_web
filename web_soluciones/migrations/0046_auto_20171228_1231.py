# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-28 17:31
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0045_auto_20171228_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucion',
            name='texto_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Texto Soluciones Ingles'),
        ),
    ]
