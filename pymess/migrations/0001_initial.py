# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-26 10:07
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
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('registration_id', models.CharField(db_index=True, max_length=256, verbose_name='registration ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('device_id', models.CharField(max_length=255, verbose_name='device ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='user_devices', to=settings.AUTH_USER_MODEL,
                                           verbose_name='user')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name_plural': 'user devices',
                'verbose_name': 'user device',
            },
        ),
    ]