from django.shortcuts import render
from Stats.sources.mlbClasses import MLB
import statsapi
# Create your views here.

aux=MLB()

def index(request):
    return render(request,'Stats/index.html',{})


def teams(request):
    teams = aux.searchTeams_by_sportId(1)['teams']
    return render(request,'Stats/teams.html',{'teams':teams})

def players(request):
    #stadisticas = aux.busca_lista_players_crit()
    return render(request,'Stats/players.html', {'players':aux.peoples})

def teamdetails(request,id):
    teamstats =aux.teamsStat(2023,1,id)
    return render(request,'Stats/teamdetails.html',{'teamstats':teamstats})