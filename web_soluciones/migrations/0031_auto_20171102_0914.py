# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0030_auto_20171030_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSolucionTagSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_palabra', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='itemsolucion',
            name='alt_seo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='itemsoluciontagseo',
            name='item_solucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_soluciones.ItemSolucion'),
        ),
        migrations.AlterUniqueTogether(
            name='itemsoluciontagseo',
            unique_together=set([('tag_palabra', 'item_solucion')]),
        ),
    ]
