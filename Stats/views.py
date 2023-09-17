from django.shortcuts import render
from Stats.sources.mlbClasses import MLB
import statsapi
# Create your views here.
aux = MLB()
def index(request):
    return render(request,'Stats/index.html',{})


def teams(request):
    teams = aux.searchTeams_by_sportId(1)['teams']
    print(teams)
    return render(request,'Stats/teams.html',{'teams':teams})

def teamdetails(request,id):
    teamstats =aux.teamsStat(2023,1,id)
    return render(request,'Stats/teamdetails.html',{'teamstats':teamstats})