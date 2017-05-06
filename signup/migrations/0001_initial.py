# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, default='profile_pic/user/default.png', upload_to='profile_pic/user')),
                ('gender', models.CharField(max_length=6)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('qualification', models.CharField(blank=True, max_length=50)),
                ('college', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('hometown', models.CharField(blank=True, max_length=50)),
                ('rel_status', models.CharField(blank=True, max_length=25)),
                ('dob', models.DateField(default='1997-01-01')),
            ],
        ),
    ]