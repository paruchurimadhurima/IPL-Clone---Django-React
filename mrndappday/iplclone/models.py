from django.conf import settings
from django.db import models
from django.utils import timezone


class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    season = models.IntegerField(null=True)
    city = models.CharField(null=True, max_length=200)
    date = models.DateField(null=True)
    team1 = models.CharField(null=True, max_length=200)
    team2 = models.CharField(null=True, max_length=200)
    toss_winner = models.CharField(null=True, max_length=200)
    toss_decision  = models.CharField(null=True, max_length=200)
    result  = models.CharField(null=True, max_length=200)
    dl_applied = models.IntegerField(null=True)
    winner = models.CharField(null=True, max_length=200)
    win_by_runs = models.IntegerField(null=True)
    win_by_wickets = models.IntegerField(null=True)
    player_of_match = models.CharField(null=True, max_length=200)
    venue = models.CharField(null=True, max_length=200)
    umpire1 = models.CharField(null=True, max_length=200)
    umpire2 = models.CharField(null=True, max_length=200)
    umpire3 = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.match_id

class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField(null=True)
    batting_team = models.CharField(max_length=200, null=True)
    bowling_team = models.CharField(max_length=200, null=True)
    over = models.IntegerField(null=True)
    ball = models.IntegerField(null=True)
    batsman = models.CharField(max_length=200, null=True)
    non_striker = models.CharField(max_length=200, null=True)
    bowler = models.CharField(max_length=200, null=True)
    is_super_over = models.IntegerField(null=True)
    wide_runs = models.IntegerField(null=True)
    bye_runs = models.IntegerField(null=True)
    legbye_runs = models.IntegerField(null=True)
    noball_runs = models.IntegerField(null=True)
    penalty_runs = models.IntegerField(null=True)
    batsman_runs = models.IntegerField(null=True)
    extra_runs = models.IntegerField(null=True)
    total_runs = models.IntegerField(null=True)
    player_dismissed = models.CharField(null=True, max_length=200)
    dismissal_kind = models.CharField(null=True, max_length=200)
    fielder = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.matchid

