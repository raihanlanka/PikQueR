from django.urls import path,include,re_path
from Leagues import views as Leagues_views



urlpatterns = [

	path("League",Leagues_views.league.as_view(),name="league"),
    path("JoinLeague",Leagues_views.joinleague.as_view(),name="joinleague"),
    re_path("FreeLeague",Leagues_views.FreeLeague,name="FreeLeague"),


    path("HotLeagueWinners",Leagues_views.HotLeagueWinners,name="HotLeagueWinners"),
    path("HotLeagueAdd",Leagues_views.HotLeague,name="HotLeague"),
    re_path("HotLeague",Leagues_views.HotLeagueplayers,name="HotLeagueplayers"),


    path("DailyLeagueWinners",Leagues_views.DailyLeagueWinners,name="DailyLeagueWinners"),
    path("DailyLeagueAdd",Leagues_views.DailyLeague,name="DailyLeague"),
    re_path("DailyLeague",Leagues_views.DailyLeagueplayers,name="DailyLeagueplayers"),
    
    path("MegaLeagueWinners",Leagues_views.MegaLeagueWinners,name="MegaLeagueWinners"),
    path("MegaLeagueAdd",Leagues_views.MegaLeague,name="MegaLeague"),
    re_path("MegaLeague",Leagues_views.MegaLeagueplayers,name="MegaLeagueplayers"),
]