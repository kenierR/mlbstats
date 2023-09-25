import statsapi as sap
import numpy as np
import pandas as pd

# peoples = sap.get('sports_players', {'season': 2023})['people']
def leadersType():
    # 'assists','shutouts','homeRuns','sacrificeBunts','sacrificeFlies','runs','groundoutToFlyoutRatio','stolenBases','battingAverage','groundOuts','numberOfPitches'
    # 'onBasePercentage','caughtStealing','groundIntoDoublePlays','totalBases','earnedRunAverage','fieldingPercentage','walksAndHitsPerInningPitched','hitByPitches' #,'flyouts',
    # 'gamesPlayed','walks','sluggingPercentage','onBasePlusSlugging','runsBattedIn','triples','extraBaseHits','hits','atBats','strikeouts','doubles','totalPlateAppearances',
    # 'intentionalWalks','wins','losses','saves','wildPitch','airOuts','balk','blownSaves','catcherEarnedRunAverage','catchersInterference','chances','completeGames','doublePlays'
    # 'earnedRun','errors','gamesFinished','gamesStarted','hitBatsman','hitsPer9Inn','holds','innings','inningsPitched','passedBalls','pitchesPerInning'#'outfieldAssists','pickoffs'
    # 'putOuts','rangeFactorPerGame','rangeFactorPer9Inn','saveOpportunities','stolenBasePercentage','strikeoutsPer9Inn','strikeoutWalkRatio','throwingErrors','totalBattersFaced','triplePlays','walksPer9Inn','winPercentage'

    return None


class MLB:#Clase de tipo singlenton, garantiza que exista una sola clase.
    __instance = None
    def __new__(cls):
        if MLB.__instance is None:
            MLB.__instance = object.__new__(cls)
        return MLB.__instance
    def __init__(self):
        self.listMetas=[]
        self.peoples = sap.get('sports_players', {'season': 2023,'sportId':1})['people']
        self.division = div = sap.get('divisions',{})
        self.teams = sap.get('teams',{})
        self.jugadores = None
        self.metas =  [
            'assists', 'shutouts', 'homeRuns', 'sacrificeBunts', 'sacrificeFlies', 'runs', 'groundoutToFlyoutRatio','stolenBases', 'battingAverage', 'groundOuts', 'numberOfPitches',
            'onBasePercentage', 'caughtStealing', 'groundIntoDoublePlays', 'totalBases', 'earnedRunAverage',
            'fieldingPercentage', 'walksAndHitsPerInningPitched', 'hitByPitches',
            'gamesPlayed', 'walks', 'sluggingPercentage', 'onBasePlusSlugging', 'runsBattedIn', 'triples',
            'extraBaseHits', 'hits', 'atBats', 'strikeouts', 'doubles', 'totalPlateAppearances',
            'intentionalWalks', 'wins', 'losses', 'saves', 'wildPitch', 'airOuts', 'balk', 'blownSaves',
            'catcherEarnedRunAverage', 'catchersInterference', 'chances', 'completeGames', 'doublePlays',
            'earnedRun', 'errors', 'gamesFinished', 'gamesStarted', 'hitBatsman', 'hitsPer9Inn', 'holds', 'innings',
            'inningsPitched', 'passedBalls', 'pitchesPerInning',
            'putOuts', 'rangeFactorPerGame', 'rangeFactorPer9Inn', 'saveOpportunities', 'stolenBasePercentage',
            'strikeoutsPer9Inn', 'strikeoutWalkRatio', 'throwingErrors', 'totalBattersFaced', 'triplePlays',
            'walksPer9Inn', 'winPercentage'


        ]#self.metas()
        self.otro = []

    def searchTeams_by_sportId(self,sport):
        return sap.get('teams',{'sportId':sport})

    def teamsStat(self,season,sportid,teamid):
        params = {'season': season, 'stats': 'season', 'group': 'hitting', 'sortStat': 'homeRuns', 'sportIds': sportid}
        teams = sap.get('teams_stats', params, force=True)['stats'][0]['splits']
        for team in teams:
            if team['team']['id'] == teamid:
                return team['stat']


    def criterio(self, funcion,parameter):
        return funcion(parameter)

    def metas(self):
        aux = []
        meta = sap.meta('leagueLeaderTypes')
        for i in meta:
            if i['displayName'] != 'pickoffs' or i['displayName'] !='outfieldAssists':
                aux.insert(len(i['displayName']),i['displayName'])
        return aux

    def ShowXRankByCat(self,top):
        aux = {}
        for x in self.metas:
            print(x)
            lideres = sap.league_leader_data(x, season=None, limit=top, leagueId=None, sportId=1)
            for i in lideres:
                print(i)

    def leaders(self,met,top):
        lideres = sap.league_leader_data(met, season=None, limit=top, leagueId=None,   sportId=1)
        print('Los {x} primeros lugares en {y}:'.format(x=top,y=met))
        data = {
            'lugar':(x[0] for x in lideres),
            'nombre':(x[1] for x in lideres),
            'team':(x[2] for x in lideres),
            'cantidad':(x[3] for x in lideres),
        }
        aux = pd.DataFrame(data)
        print(aux)
        return lideres

    def rankOf(self,jug,top):
        aux = {}
        datos = {}
        lista = []
        for meta in self.metas:
            lideres = self.leaders(meta,top)
            for x in lideres:
                if jug['fullName'] == x[1]:
                    aux = {'jugador':x,'meta':meta}
                    datos = {'Jugador':x[1],'Meta':meta,'Lugar':x[0],'Cantidad':x[3]}
                    lista.insert(len(datos),datos)
        return lista

    def ShowRank(self,p,top):
        listaMetas = aux.rankOf(aux.buscarPlayer(p),top)
        data = {
            'Lugar':(x['Lugar'] for x in listaMetas),
            'Criterio':(x['Meta'] for x in listaMetas),
            'Cantidad':(x['Cantidad'] for x in listaMetas)
        }
        df = pd.DataFrame(data)
        print(df.to_string())

    def bat(self, b):
        players = []
        for x in self.peoples:
            try:
                if x['batSide']['code'] == b:
                    players.insert(len(x), x)
            except:
                pass
        self.peoples = players
        return players

    def pos(self, pos):
        players = (x for x in self.peoples if x['primaryPosition']['abbreviation'] == pos)
        self.peoples = players
        return players

    def NotPos(self, pos):
        players = (x for x in self.peoples if x['primaryPosition']['abbreviation'] != pos)
        self.peoples = players
        return players

    def born(self, city):
        players = []
        for x in self.peoples:
            # print(type(x['primaryNumber']))
            try:
                if x['birthCountry'] == city:
                    players.insert(len(x), x)
            except:
                pass
        self.peoples = players
        return players

    def NotBorn(self, city):
        players = []
        for x in self.peoples:
            # print(type(x['primaryNumber']))
            try:
                if x['birthCountry'] != city:
                    players.insert(len(x), x)
            except:
                pass
        self.peoples = players
        return players

    def edad(self,edad):
        players = []
        izq = edad.split(" ")[0]
        der = int(edad.split(' ')[1])
        if izq == '=':
            for x in self.peoples:
                # print(type(x['primaryNumber']))
                try:
                    if x['currentAge'] == der:
                        players.insert(len(x), x)
                except:
                    pass
        elif izq == '<':
            for x in self.peoples:
                try:
                    if x['currentAge'] < der:
                        players.insert(len(x), x)
                except:
                    pass
        elif izq == '>':
            for x in self.peoples:
                try:
                    if x['currentAge'] > der:
                        players.insert(len(x), x)
                except:
                    pass
        self.peoples = players
        return players

    def trow(self, t):
        players = []
        for x in self.peoples:
            try:
                if x['pitchHand']['code'] == t:
                    players.insert(len(x), x)
            except:
                pass
        self.peoples = players
        return players
    def searchTeamByID(self,id):
        aux  = None
        for i in self.teams['teams']:
            if i['id'] == id:
                aux = i['name']
        return aux
    def searchDivByTeamId(self,id):
        aux = None
        for i in self.teams['teams']:
            if i['id'] == id:
                aux = i['division']['name']
        return aux
    def searchDivId_ByTeamId(self,id):
        #print(id)
        aux = None
        for i in self.teams['teams']:
            if i['id'] == id:
                aux = i['division']['id']

        for x in self.division['divisions']:
            if x['id'] == aux:
                aux = x['nameShort']
        return aux
    def searchDivShortNameById(self,id):
        aux = None
        for x in self.division:
            if x['id'] == id:
                aux = x['nameShort']
        return aux
    def div(self, div):
        players = []
        for x in self.peoples:
            try:
                league = self.searchDivByTeamId(x['currentTeam']['id']) #sap.get('team', {'teamId': x['currentTeam']['id']})['teams'][0]['division']['name']

                if league == div:
                    players.insert(len(x), x)
            except:
                pass
        self.peoples = players
        return players
    def team(self,t):
        players = []
        teamsId = sap.lookup_team(t)[0]['id']
        for x in self.peoples:

            try:
                if x['currentTeam']['id'] == teamsId:

                    players.insert(len(x), x)

            except:
                pass
        self.peoples = players
        return players
    def NotTeam(self,t):
        players = []
        teamsId = sap.lookup_team(t)[0]['id']
        for x in self.peoples:

            try:
                if x['currentTeam']['id'] != teamsId:

                    players.insert(len(x), x)

            except:
                pass
        self.peoples = players
        return players
    def resultadoJugador(self,jug):
        jugadorTeam = sap.lookup_player(jug)[0]['currentTeam']['id']
        scheduleId = sap.last_game(jugadorTeam)
        box = sap.boxscore(scheduleId)
        print(box)

    def teamById(self,id):
        name = None
        for i in self.teams['teams']:
            if i['id'] == id:
                name = i['name']
        return name

    def Show(self):
        # H = ( x['id'] for x in self.peoples )
        # sap.player_stat_data(id, group="[hitting,pitching,fielding]", type="season", sportId=1)
        data = {
            "Nombre":(x['fullName'] for x in self.peoples),
            "Div":(self.searchDivId_ByTeamId(x['currentTeam']['id']) for x in self.peoples),
            "Team":(self.searchTeamByID(x['currentTeam']['id']) for x in self.peoples),
            "Edad":(x['currentAge'] for x in self.peoples),
            "Posicion":(x['primaryPosition']['abbreviation'] for x in self.peoples),
            "Pais":(x['birthCountry'] for x in self.peoples),
            #"H":(( sap.player_stat_data(x['id'],group="[hitting,pitching,fielding]", type="season", sportId=1)['stats'][0]['stats']['hits'] if self.peoples['primaryPosition']['abbreviation'] !='P' else 0) for x in self.peoples)
        }
        df = pd.DataFrame(data)
        print(df.to_string())


        #     print(x['fullName'], '-------',sap.get('team', {'teamId': x['currentTeam']['id']})['teams'][0]['division']['name'],'-------',
        #           sap.lookup_team(x['currentTeam']['id'])[0]['name'],'-----',
        #           x['currentAge'],'----',
        #           x['primaryPosition']['abbreviation'],'----',
        #           x['birthCountry']
        #           )
        #
        # print('---------------------------------------------------------------------------------------------------------')
        # print(len(self.peoples))
    def buscarPlayer(self,p):
        aux = sap.lookup_player(p)

        return aux[0]
    def BuscaNombres(self):
        nombres = []
        c = input('entre un nombre !/@/# para cancelar/aceptar/empezar:')
        aux = c
        while c !='!':
            for x in self.peoples:
                if aux in x['fullName']:
                    nombres.insert(len(x),x)
                    print(x['fullName'])
            print(aux+'>')
            c = input(':')
            if c == '@':
                player = sap.lookup_player(aux)[0]
                player_stat= sap.player_stat_data(player['id'])
                print(pd.DataFrame(player_stat['stats'][0]))
            aux = aux + c
            if c == '#':
                aux = ''

    def iterate(self,k, to_iterate):

        if isinstance(to_iterate, dict):
            for key, value in to_iterate.items():
                if key == k:
                    self.otro.insert(len(self.otro), value)
                else:
                    self.iterate(k, to_iterate[key])
        elif isinstance(to_iterate, list):
            for key in to_iterate:
                self.iterate(k, key)
        return self.otro

    def busca_lista_crit(self,l, to_find):
        list_crit = {}
        for x in l:
            list_crit[x] = self.iterate(x, to_find)
            #print(self.iterate(x, to_find))
            self.otro = []
        return list_crit



    def busca_lista_players_crit(self,l,lp):
        list_players = {}
        for x in lp:
            try :
                personId = sap.lookup_player(x)[0]['id']
                person = sap.player_stat_data(personId, group="[hitting]", type="season", sportId=1)
                list_players[x] = self.busca_lista_crit(l, person)
            except:
                list_players[x] = 'Not active player'


        return list_players



aux = MLB()
# personId = sap.lookup_player('Aaron Judge')[0]['id']
# person = sap.player_stat_data(personId, group="[hitting,pitching,fielding]", type="season", sportId=1)

# person = {'otro':[{'runs':15},6],'b':{ 'runs':30}}
# aux1 = {'a':6,'runs':4}

# playersList = [
#     'Aaron Judge',
#     'Mookie Betts',
#     'Freddie Freeman',
#     'Kyle Tucker',
#     'Ronald Acuña Jr.',
#     'Yordan Alvarez'
# ]
# crit_list = ['gamesPlayed','runs','avg','homeRuns','hits']
# to_ptr = aux.busca_lista_players_crit(crit_list,playersList)
# df = pd.DataFrame(to_ptr)
# print(df.to_string())
# print(to_ptr)




# aux.BuscaNombres() #Busca jugadores a partir de su nombre y da su estadistica

# lideres por categorias
# aux.ShowRank('Shohei Ohtani',3)# muestra en que categoria esta el jugador entre los 3 primeros
# aux.ShowXRankByCat(3) # muestra los 3 primeros lugares para todas las categorias
# aux.leaders('hits',20)# muestra los 15 primeros de una categorias
# listaMetas = aux.rankOf(aux.buscarPlayer('Freddie Freeman'))
#
# for i in listaMetas:
#
#     print(i['Lugar'],i['Meta'],i['Cantidad'])
#
# x=aux.criterio(aux.bat,'L')
# x=aux.criterio(aux.trow,'L')
# x=aux.criterio(aux.edad,'= 30')
# # x=aux.criterio(aux.team,'Milwaukee Brewers')
# x=aux.criterio(aux.div,'American League Central')
# # x = aux.criterio(aux.pos,'P')
# x = aux.criterio(aux.team,'Washington Nationals')
# x=aux.criterio(aux.born,'USA')

# x=aux.criterio(aux.NotTeam,'Baltimore Orioles')
#aux.Show()

# print(aux.searchTeamByID(4124))
# print(aux.searchDivByTeamId(117))
# aux.resultadoJugador('Aaron Judge')





