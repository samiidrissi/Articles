# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonSiteWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='soustitre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]