# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import tinymce.models
import web_casos_exito.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasoExito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion_corta', models.TextField(blank=True, null=True)),
                ('descripcion', tinymce.models.HTMLField(blank=True, default='Descripción de este Caso de Éxito', null=True, verbose_name='Descripción')),
                ('orden', models.PositiveIntegerField(default=0)),
                ('industria', models.CharField(blank=True, default='', max_length=120)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('imagen_principal', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_casos_exito.models.CasoExito.imagen_principal_upload_to, verbose_name='Imagen Caso Éxito (400x200)')),
            ],
            options={
                'verbose_name': 'Caso de Éxito',
                'verbose_name_plural': 'Casos de Éxito',
            },
        ),
        migrations.CreateModel(
            name='CasoExitoImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_agua', models.PositiveIntegerField(choices=[(0, 'Ninguna'), (1, 'Blanca'), (2, 'Naranja')], default=2)),
                ('orden', models.PositiveIntegerField(default=0)),
                ('alt_seo', models.CharField(blank=True, default='', max_length=125, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_casos_exito.models.CasoExitoImagen.imagen_upload_to, verbose_name='Imagen Caso de Exito')),
                ('caso_exito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_imagenes', to='web_casos_exito.CasoExito')),
            ],
        ),
        migrations.CreateModel(
            name='CasoExitoVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=500)),
                ('orden', models.PositiveIntegerField(default=0)),
                ('caso_exito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_videos', to='web_casos_exito.CasoExito')),
            ],
        ),
    ]
