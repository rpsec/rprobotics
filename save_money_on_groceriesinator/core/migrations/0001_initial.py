# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredList', models.TextField()),
                ('directions', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
    ]
