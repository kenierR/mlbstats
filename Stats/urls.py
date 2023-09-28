
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
    path('updivisions/',views.updivisions,name='updivisions')
]

