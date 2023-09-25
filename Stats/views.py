from django.shortcuts import render
from Stats.sources.mlbClasses import MLB
import statsapi
from Stats.models import *
# Create your views here.

aux=MLB()

def index(request):
    return render(request,'Stats/index.html',{})

def uppositions(request):
    pos = sap.meta('positions')
    for x in pos :
        dbPos = Position(**x)
        dbPos.save()
    return render(request,'Stats/uppositions.html',{'pos':pos})

def upseasons(request):
    sportIds = Sport.objects.all()
    lsport = list(sportIds)
    #print(lsport[0].id)
    for sport in lsport:
        for seasonId in range(1900,2050):
            try:
                season = sap.get('season',{'sportId':sport.id,'divisionId':'','leagueId':'','seasonId':seasonId})['seasons'][0]
                if len(season) > 0 :
                    dbseason = Season(**season)
                    dbseason.save()
            except:
                pass

    return render(request,'Stats/upseasons.html',{})

def teams(request):

    teams = aux.searchTeams_by_sportId(1)['teams']
    return render(request,'Stats/teams.html',{'teams':teams})

def players(request):
    listaplayer = list(x['fullName'] for x in aux.peoples)[0:10]
    print(listaplayer)
    crit = ['runs','hits','homeRuns']
    pruebaplayer = statsapi.lookup_player('Aaron Judge')
    stadisticas = aux.busca_lista_players_crit(crit,listaplayer)
    print((stadisticas))
    return render(request,'Stats/players.html', {'players':listaplayer,'stats':stadisticas})

def teamdetails(request,id):
    listaplayer = list(x['fullName'] for x in aux.peoples)


    crit = ['runs', 'hits']
    stadisticas = aux.busca_lista_players_crit(crit, listaplayer)
    teamstats =aux.teamsStat(2023,1,id)
    return render(request,'Stats/teamdetails.html',{'teamstats':teamstats,'stats':stadisticas})