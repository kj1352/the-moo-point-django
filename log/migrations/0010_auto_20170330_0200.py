# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0009_auto_20170330_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='usn',
        ),
        migrations.AddField(
            model_name='contactus',
            name='text',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
