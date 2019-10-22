from django.urls import path
from iplclone.views.iplclone.match_api import *
from iplclone.views.iplclone.season_api import *
from iplclone.views.iplclone.delivery_api import *
from iplclone.views.iplclone.operations_api import *

urlpatterns = [
    path('api/v1/matches/', MatchesList.as_view(), name="matches-all"),
    path('api/v1/matches/<int:pk>/', MatchDetail.as_view(), name="match-detail"),
    path('api/v1/matches/seasons/', SeasonsList.as_view(), name="seasons-all"),
    path('api/v1/matches/seasons/<int:season>/', SeasonDetail.as_view(), name="season-details"),
    path('api/v1/matches/deliveries/', DeliveriesList.as_view(), name="deleveries-all"),
    path('api/v1/matches/<int:pk>/deliveries/', DeliveryDetail.as_view(), name="delivery-detail"),
    path('api/v1/matches/<int:pk>/deliveries/top_run_scorer/', top_run_scorers, name="top-scorer-detail"),
    path('api/v1/matches/<int:pk>/deliveries/top_wicket_takers/', top_wicket_takers, name="top-wicket-takers"),
    path('api/v1/matches/<int:pk>/deliveries/extras_conceded/', extras_conceded, name="extras-conceded"),
    path('api/v1/matches/<int:pk>/deliveries/innings/<int:no>', inning, name="innings-match-details")
]