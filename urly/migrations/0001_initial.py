# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('short', models.CharField(max_length=255, serialize=False, verbose_name='Short url', primary_key=True)),
                ('url', models.CharField(max_length=2048, verbose_name='Original url', db_index=True)),
            ],
        ),
    ]
