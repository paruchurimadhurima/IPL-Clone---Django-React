from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from iplclone.models import *
from iplclone.serializers.match_serializer import *
from iplclone.serializers.delivery_serializer import *
from django.db.models import *


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def top_run_scorers(request, pk):
    """
    get top three run scorers
    """
    players_list = Delivery.objects.filter(match_id=pk).values('batsman', 'batting_team').annotate(batsman_runs=Sum('batsman_runs')).order_by('-batsman_runs')[:3]
    serializer = DeliverySerializer(players_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def top_wicket_takers(request, pk):
    """
    get top three wicket scorers
    """
    players_list = Delivery.objects.filter(match_id=pk).exclude(dismissal_kind="").values('bowler', 'bowling_team').annotate(total_runs=Count('dismissal_kind')).order_by('-total_runs')[:3]
    serializer = DeliverySerializer(players_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def extras_conceded(request, pk):
    """
    extras conceded for a team
    """
    innings = Delivery.objects.filter(match_id=pk).values('batting_team').annotate(total_runs=Sum('extra_runs')).order_by('-total_runs')
    serializer = DeliverySerializer(innings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def inning(request, pk, no):
    """
    get innings
    """
    innings = Delivery.objects.filter(match_id=pk).filter(inning=no)
    serializer = DeliverySerializer(innings, many=True)
    return Response(serializer.data)

