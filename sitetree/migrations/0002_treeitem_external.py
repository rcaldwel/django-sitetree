# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treeitem',
            name='external',
            field=models.BooleanField(default=False, help_text='If enabled link will open in a new window', verbose_name='Open URL in new window'),
        ),
    ]
