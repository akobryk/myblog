# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 10:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Date of birthday')),
                ('mobile_phone', models.CharField(blank=True, default='', max_length=12, verbose_name='Mobile Phone')),
                ('skype', models.CharField(blank=True, max_length=120, verbose_name='Skype')),
                ('about_me', models.TextField(blank=True, verbose_name='About me')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]