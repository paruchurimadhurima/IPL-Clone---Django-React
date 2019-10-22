from django.http import Http404
from iplclone.serializers.season_serializer import SeasonSerializer
from iplclone.serializers.match_serializer import MatchSerializer
from iplclone.models import Match
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class SeasonsList(APIView):
    """
    List all Seasons.
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        seasons = Match.objects.values('season').distinct().order_by('-season')
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data)

class SeasonDetail(APIView):
    """
    Retrieve match instance.
    """
    permission_classes = (permissions.AllowAny,)

    def get_object(self, season):
        try:
            return Match.objects.filter(season=season)
        except Match.DoesNotExist:
            raise Http404

    def get(self, request, season, format=None):
        match = self.get_object(season)
        serializer = MatchSerializer(match, many=True)
        return Response(serializer.data)




