# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 20:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_auto_20170330_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]