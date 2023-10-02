from django.shortcuts import render
from Stats.sources.mlbClasses import MLB
import statsapi
from Stats.models import *
# Create your views here.

aux=MLB()

def index(request):
    return render(request,'Stats/index.html',{})

def upplayers(request):
    sports = Sport.objects.all()
    lsport = list(sports)
    seasons = Season.objects.all()
    lseasons = range(1960,2024)#list(seasons)
    for season in lseasons:
        for sport in lsport:
            print('season',season,'sport',sport)
            players = sap.get('sports_players', {'season': season, 'sportId': sport})['people']
            #print(players['id'])
            if len(players)>0:
                for p in players:
                    try:
                        teams = Teams.objects.get(pk=p['currentTeam']['id'])
                        print(p['fullName'],'si -----',p['id'])

                    except Teams.DoesNotExist:
                        print('salvado  ---------------------------***********------', season, sport,p['fullName'],'teams:',p['currentTeam']['id'])
                        dbTeams = Teams(id=p['currentTeam']['id'],name=p['currentTeam']['name']).save()

                    except Position.DoesNotExist:
                        print('esa posicion no existe en bd',p['primaryPosition']['code'])

                    finally:
                        teams = Teams.objects.get(pk=p['currentTeam']['id'])
                        positions = Position.objects.get(pk=p['primaryPosition']['code'])
                        p['currentTeam'] = teams
                        p['primaryPosition'] = positions
                        try:
                            p['batSide'] = p['batSide']['code']
                        except :
                            pass
                        try:
                            p['pitchHand'] = p['pitchHand']['code']
                        except:
                            pass
                        dbplayer = Player(**p)
                        dbplayer.save()


            else:
                print('no existen player en esa temporada para ese deporte',season,sport.id)

    return render(request,'Stats/upplayers.html',{})
def upteams(request):
    teams = sap.get('teams', {})['teams']
    for tm in teams:
        print(tm['teamName'],tm['id'])
        try:
            sprinleague = League.objects.get(pk=tm['springLeague']['id'])
            tm['springLeague'] = sprinleague
        except:
            pass
        try:
            springvenue = Venue.objects.get(pk=tm['springVenue']['id'])
            tm['springVenue']=springvenue
        except:
            pass

        season = Season.objects.get(pk=tm['season'])
        tm['season'] = season

        try:
            venue = Venue.objects.get(pk=tm['venue']['id'])
            tm['venue'] = venue
        except:
            dbvenue = Venue(id=tm['venue']['id'])
            dbvenue.save()
            venue = Venue.objects.get(pk=tm['venue']['id'])
            tm['venue'] = venue

        try:
            league = League.objects.get(pk=tm['league']['id'])
            tm['league'] = league
        except:
            league = League(id=7777)
            tm['league'] = league
        try:
            division = Division.objects.get(pk=tm['division']['id'])
            tm['division'] = division
        except :
            division = Division(id=7777)
            tm['division'] = division

        try:
            sport = Sport.objects.get(pk=tm['sport']['id'])
            tm['sport'] = sport
        except:
            dbsport = Sport(id=tm['sport']['id'],name=tm['sport']['name'])
            dbsport.save()
            sport = Sport.objects.get(pk=tm['sport']['id'])
            tm['sport'] = sport

        dbteams = Teams(**tm)
        dbteams.save()
    return render(request,'Stats/upteams.html',{})
def updivisions(request):
    divisions = sap.get('divisions', {})['divisions']
    for div in divisions:
        season = Season.objects.get(pk=div['season'])
        div['season'] = season

        league = League.objects.get(pk=div['league']['id'])
        print(div['id'])
        div['league'] = league

        sport = Sport.objects.get(pk=div['sport']['id'])
        div['sport'] = sport

        dbdivisions = Division(**div)
        dbdivisions.save()
    return render(request,'Stats/updivisions.html',{})
def upleagues(request):
    league = sap.get('league', {'sportId': '', 'leagueIds': ''})['leagues']
    sport = Sport()
    for lg in league:
        try:
            season = Season.objects.get(pk=lg['seasonDateInfo']['seasonId'])
            lg['season'] = season
            del (lg['seasonDateInfo'])
        except Season.DoesNotExist:
            dbseason = Season(seasonId=lg['seasonDateInfo']['seasonId'])
            dbseason.save()
            season = Season.objects.get(pk=lg['seasonDateInfo']['seasonId'])
            lg['season'] = season
            del (lg['seasonDateInfo'])
        try:
            sport = Sport.objects.get(pk=lg['sport']['id'])
        except Sport.DoesNotExist:
            dbsport = Sport(id=lg['sport']['id'])
            dbsport.save()
            sport = Sport.objects.get(pk=lg['sport']['id'])
        except:
            sport = Sport(id=7777)



        lg['sport']=sport
        dbleague = League(**lg)
        dbleague.save()
    return render(request,'Stats/upleagues.html',{})
def upvenues(request):
    venue = sap.get('venue',{'venueIds':'','seasonId':2023})['venues']
    for vn in venue:
        season = Season(seasonId=vn['season'])
        vn['season'] = season
        dbvenue = Venue(**vn)
        dbvenue.save()
    return render(request,'Stats/upvenues.html',{})
def upsports(request):
    sport = sap.get('sports',{})['sports']
    for sp in sport:
            print(sp)
        #try:
            dbsport = Sport(**sp)
            dbsport.save()
        #except:
            pass
    return render(request,'Stats/upsports.html',{})
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
                season['sportId'] = sport.id
                if len(season) > 0 :
                    print(season['sportId'],season['seasonId'])
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