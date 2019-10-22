from iplclone.models import *
from rest_framework import serializers

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('match_id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner' ,'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs', 'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2', 'umpire3')

