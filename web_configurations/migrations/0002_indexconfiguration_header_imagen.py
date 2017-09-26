# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 15:55
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields
import web_configurations.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexconfiguration',
            name='header_imagen',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_configurations.models.IndexConfiguration.header_imagen_upload_to, verbose_name='Imagen Cabezote'),
        ),
    ]
