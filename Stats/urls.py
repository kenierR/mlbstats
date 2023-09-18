
from django.urls import path,include
from Stats import views
#direccion es del proyecto

app_name = 'Stats'
urlpatterns = [
    path('',views.index,name='index'),
    path('teams/',views.teams,name='teams'),
    path('teamdetails/<int:id>',views.teamdetails,name='teamdetails'),
    path('players/',views.players,name='players')
]

