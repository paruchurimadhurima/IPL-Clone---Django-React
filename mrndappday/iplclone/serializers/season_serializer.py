from iplclone.models import *
from rest_framework import serializers

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('season' ,)
