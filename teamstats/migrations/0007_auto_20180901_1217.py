# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-01 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamstats', '0006_auto_20180829_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goals', models.IntegerField()),
                ('away_goals', models.IntegerField()),
                ('away_team', models.ManyToManyField(related_name='away_match', to='teamstats.TournamentPlayer')),
                ('home_team', models.ManyToManyField(related_name='home_match', to='teamstats.TournamentPlayer')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamstats.Tournament')),
            ],
        ),
        migrations.RemoveField(
            model_name='tournamentplayerpoints',
            name='tournamentplayer',
        ),
        migrations.DeleteModel(
            name='TournamentPlayerPoints',
        ),
    ]
