# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
    ]
