# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import web_soluciones.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0008_auto_20170926_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSolucionImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField()),
                ('imagen', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_soluciones.models.ItemSolucionImagen.imagen_upload_to, verbose_name='Imagen Item Solución')),
                ('item_solucion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_imagenes', to='web_soluciones.ItemSolucion')),
            ],
        ),
    ]
