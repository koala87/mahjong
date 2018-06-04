# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='score2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='score3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='score4',
            field=models.IntegerField(default=0),
        ),
    ]
