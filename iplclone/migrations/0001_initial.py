# Generated by Django 2.2.2 on 2019-06-17 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('season', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(null=True)),
                ('team1', models.CharField(max_length=200, null=True)),
                ('team2', models.CharField(max_length=200, null=True)),
                ('toss_winner', models.CharField(max_length=200, null=True)),
                ('toss_decision', models.CharField(max_length=200, null=True)),
                ('result', models.CharField(max_length=200, null=True)),
                ('dl_applied', models.IntegerField(null=True)),
                ('winner', models.CharField(max_length=200, null=True)),
                ('win_by_runs', models.IntegerField(null=True)),
                ('win_by_wickets', models.IntegerField(null=True)),
                ('player_of_match', models.CharField(max_length=200, null=True)),
                ('venue', models.CharField(max_length=200, null=True)),
                ('umpire1', models.CharField(max_length=200, null=True)),
                ('umpire2', models.CharField(max_length=200, null=True)),
                ('umpire3', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField(null=True)),
                ('batting_team', models.CharField(max_length=200, null=True)),
                ('bowling_team', models.CharField(max_length=200, null=True)),
                ('over', models.IntegerField(null=True)),
                ('ball', models.IntegerField(null=True)),
                ('batsman', models.CharField(max_length=200, null=True)),
                ('non_striker', models.CharField(max_length=200, null=True)),
                ('bowler', models.CharField(max_length=200, null=True)),
                ('is_super_over', models.IntegerField(null=True)),
                ('wide_runs', models.IntegerField(null=True)),
                ('bye_runs', models.IntegerField(null=True)),
                ('legbye_runs', models.IntegerField(null=True)),
                ('noball_runs', models.IntegerField(null=True)),
                ('penalty_runs', models.IntegerField(null=True)),
                ('batsman_runs', models.IntegerField(null=True)),
                ('extra_runs', models.IntegerField(null=True)),
                ('total_runs', models.IntegerField(null=True)),
                ('player_dismissed', models.CharField(max_length=200, null=True)),
                ('dismissal_kind', models.CharField(max_length=200, null=True)),
                ('fielder', models.CharField(max_length=200, null=True)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iplclone.Match')),
            ],
        ),
    ]