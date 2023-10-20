
from django.urls import path,include
from Stats import views
#direccion es del proyecto

app_name = 'Stats'
urlpatterns = [
    path('',views.index,name='index'),
    path('teams/',views.teams,name='teams'),
    path('teamdetails/<int:id>',views.teamdetails,name='teamdetails'),
    path('players/',views.players,name='players'),
    path('uppositions/',views.uppositions,name='uppositions'),
    path('upseason/',views.upseasons,name='upseasons'),
    path('upsports/',views.upsports,name='upsports'),
    path('upvenues/',views.upvenues,name='upvenues'),
    path('upleagues/',views.upleagues,name='upleagues'),
    path('updivisions/',views.updivisions,name='updivisions'),
    path('upteams/',views.upteams,name='upteams'),
    path('upplayers/',views.upplayers,name='upplayers'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('up_team_season/',views.up_team_season,name='up_team_season'),
    path('up_player_team/',views.up_player_team,name='up_player_team'),
]

