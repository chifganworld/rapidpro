# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0093_populate_translatables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='language_dict',
        ),
        migrations.RemoveField(
            model_name='broadcast',
            name='media_dict',
        ),
        migrations.RemoveField(
            model_name='broadcast',
            name='text',
        ),
    ]
