# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171030_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=True, help_text='Verify if the user is teacher or student', verbose_name='Is Teacher?'),
        ),
    ]