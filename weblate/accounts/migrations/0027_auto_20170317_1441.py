# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_profile_special_chars'),
        ('permissions', '0004_auto_20170317_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autogroup',
            name='group',
        ),
        migrations.DeleteModel(
            name='AutoGroup',
        ),
    ]
