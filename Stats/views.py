from django.shortcuts import render
from Stats.sources.mlbClasses import MLB
import statsapi
from Stats.models import *


#from .forms import TeamSelectForm
# Create your views here.

aux=MLB()

def index(request):
    return render(request,'Stats/index.html',{})

def up_player_team(request):
    equipos = Teams.objects.filter(sport=1)
    sea = Season.objects.all()
    for t in equipos:
        print(t.name,t.id)
        for s in sea:
            try:
                roster = sap.get('team_roster',{'teamId':t.id,'season':s.seasonId,'rosterType':'fullSeason'})['roster']
                for r in roster:
                    print(r['person']['id'])
                    player = Player.objects.get(pk=r['person']['id'])

                    player.team.add(t)
                    print(player.name,t.seasonId)
            except:
                print(t.id,t.name,s.seasonId,'NO tiene roster')

    return render(request,'Stats/up_player_team.html',{})
def up_team_season(request):
    dbseason = Season.objects.all()
    for season in dbseason:
        teams = sap.get('teams', {'season': season.seasonId})['teams']
        for team in teams:
            try:
                dbteam = Teams.objects.get(pk=team['id'])
                dbteam.season.add(season)
                print(team['id'], season,'sii')
            except:
                dbteam = Teams(id=team['id']).save()
                dbteam = Teams.objects.get(pk=team['id'])
                dbteam.season.add(season)
                print(team['id'], season,'nooo')
    return render(request,'Stats/up_team_season.html',{})
def dashboard(request):
    return render(request,'Stats/dashboard.html',{})
def upplayers(request):
    sports = Sport.objects.all()
    #lsport = list(sports)
    seasons = Season.objects.all()
    lseasons = range(2019,2024)#list(seasons)
    for season in lseasons:
        for sport in sports:
            print('season',season,'sport',sport.id)
            players = sap.get('sports_players', {'season': season, 'sportId': sport.id})['people']
            team = ''
            #print(players['id'])
            if len(players)>0:
                for p in players:
                    print(p['fullName'])
                    #print(p)
                    try:
                        team = Teams.objects.get(pk=p['currentTeam']['id'])
                        del(p['currentTeam'])
                        print(p['fullName'],'si -----',p['id'],season,sport)
                    except KeyError:
                        pos = Position.objects.get(pk=p['primaryPosition']['code'])
                        p['primaryPosition'] = pos
                    except Teams.DoesNotExist:
                        try:
                            team = Teams(id=p['currentTeam']['id'],name=p['currentTeam']['name']).save()
                        except:
                            team = Teams.objects.get(pk=77777)
                        finally:
                            del(p['currentTeam'])
                    finally:
                        pos = Position.objects.get(pk=p['primaryPosition']['code'])
                        p['primaryPosition'] = pos

                    try:
                        p['batSide'] = p['batSide']['code']
                    except:
                        pass

                    try:
                        p['pitchHand'] = p['pitchHand']['code']
                    except:
                        pass


                    Player(**p).save()
                    pl = Player.objects.get(pk=p['id'])
                    print(team)
                    pl.team.add(team)
                    pl.season.add(season)

            else:
                print('no existen player en esa temporada para ese deporte',season,sport.id)

    return render(request,'Stats/upplayers.html',{})
def upteams(request):
    sea = Season.objects.all()
    for s in sea:
        teams = sap.get('teams', {'season':s})['teams']
        for tm in teams:
            print(s.seasonId)
            try:
                print(tm['name'],tm['id'],'-> Working..........')
            except:
                pass

            try:
                sprinleague = League.objects.get(pk=tm['springLeague']['id'])
                tm['springLeague'] = sprinleague
                print('tiene springLeague.')
            except:
                print('No tiene springLeague','Saliendo......')

            try:
                springvenue = Venue.objects.get(pk=tm['springVenue']['id'])
                tm['springVenue']=springvenue
                print('tiene springVenue')
            except:
                print('No tiene springVenue','Saliendo......')

            #season = Season.objects.get(pk=tm['season'])
            #tm['season'] = s

            try:
                del(tm['conference'])
            except:
                pass


            try:
                venue = Venue.objects.get(pk=tm['venue']['id'])
                tm['venue'] = venue
                print('tiene venue.')
            except Venue.DoesNotExist:
                dbvenue = Venue(id=tm['venue']['id'])
                dbvenue.save()
                venue = Venue.objects.get(pk=tm['venue']['id'])
                tm['venue'] = venue
                print('No tiene venue', 'Saliendo......')
            except KeyError:
                pass


            try:
                league = League.objects.get(pk=tm['league']['id'])
                tm['league'] = league
                print('tiene league.')
            except:
                league = League(id=7777)
                tm['league'] = league
                print('No tiene league', 'Saliendo......')

            try:
                division = Division.objects.get(pk=tm['division']['id'])
                tm['division'] = division
                print('tiene division.')
            except :
                division = Division(id=7777)
                tm['division'] = division
                print('No tiene division', 'Saliendo......')

            try:
                sport = Sport.objects.get(pk=tm['sport']['id'])
                print('sport: ',sport.id,': Existe en la base de datos...')
                try:
                    tm['sport'] = sport
                    print('sport: ',sport.id,': Existe en la bd y se agrega el sport')
                except:
                    del(tm['sport'])
                    print(sport.id, 'No existe el sport y se elimia')

            except :
                try:
                    print('sport: ',sport.id,'No existe en la bd y se agrega')
                    dbsport = Sport(id=tm['sport']['id'], name=tm['sport']['name']).save()
                    sport = Sport.objects.get(pk=tm['sport']['id'])
                    tm['sport'] = sport
                    print('No tiene sport', '......')
                except:
                    print('sport: ',sport.id,'No esta en la bd y no existe el sport ')




            del(tm['season'])
            dbteams = Teams(**tm).save()
            dbteams = Teams.objects.get(pk=tm['id'])
            print(s.seasonId)
            dbteams.season.add(s)

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
    for sp in lsport:
        for seasonId in range(1900,2025):
            try:
                season = sap.get('season',{'sportId':sp.id,'divisionId':'','leagueId':'','seasonId':seasonId})['seasons'][0]
                #season['sportId'] = sp
                print(sp.id, seasonId,'....')
                if len(season) > 0 :
                    dbseason = Season(seasonId=seasonId).save()
                    del(season['seasonId'])
                    dbseason = Season.objects.get(seasonId=seasonId)
                    dbseason.sportId.add(sp,through_defaults=season)
                    print(sp.id, seasonId,'saved..')
            except:
                print(sp.id, seasonId,'erorr....')

    return render(request,'Stats/upseasons.html',{})
def teams(request):
    context = {}
    teams = aux.searchTeams_by_sportId(1)['teams']
    form = TeamSelectForm(request.POST or None)
    context['form'] = form
    context['teams'] = teams
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("name")
            print(temp)
    return render(request,'Stats/teams.html',context)
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