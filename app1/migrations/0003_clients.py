# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-02 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_delete_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=254, unique=True)),
                ('LAST_NAME', models.CharField(max_length=254)),
                ('E_MAIL', models.CharField(max_length=254)),
            ],
        ),
    ]
