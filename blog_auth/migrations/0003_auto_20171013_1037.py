# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_auth', '0002_auto_20171013_1036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UProfile',
            new_name='UserProfile',
        ),
    ]
