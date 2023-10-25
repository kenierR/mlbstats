from django.db import models
import statsapi as sap
from Stats.sources.mlbClasses import MLB
# Create your models here.
aux = MLB()
class Teams(models.Model):#hecho
    id = models.IntegerField(primary_key=True, unique=True, blank=False)
    season = models.ManyToManyField('Season', null=True)
    name = models.CharField(max_length=50, null=True)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True)
    league = models.ForeignKey('League', on_delete=models.CASCADE, null=True)
    division = models.ForeignKey('Division', on_delete=models.CASCADE, null=True)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True)
    springLeague = models.ForeignKey('League', on_delete=models.CASCADE, null=True, related_name='springLeague')
    springVenue = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True, related_name='springVenue')
    allStarStatus = models.CharField(max_length=1,null=True,blank=True)
    link = models.CharField(max_length=50, null=True,blank=True)
    teamCode = models.CharField(max_length=10,null=True,blank=True)
    fileCode = models.CharField(max_length=10,null=True,blank=True)
    abbreviation = models.CharField(max_length=10,null=True,blank=True)
    teamName = models.CharField(max_length=50,null=True,blank=True)
    locationName = models.CharField(max_length=50,null=True,blank=True)
    firstYearOfPlay = models.CharField(max_length=4,null=True,blank=True)
    shortName = models.CharField(max_length=50,null=True,blank=True)
    parentOrgName = models.CharField(max_length=50,null=True,blank=True)
    parentOrgId = models.IntegerField(null=True,blank=True)
    franchiseName = models.CharField(max_length=50,null=True,blank=True)
    clubName = models.CharField(max_length=50,null=True,blank=True)
    active = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return str(self.id) +'  '+ self.name
class Venue(models.Model):#hecho
    id = models.IntegerField(primary_key=True,unique=True,blank=False)
    name = models.CharField(max_length=55,null=True)
    link  = models.CharField(max_length=50,null=True)
    active = models.BooleanField(null=True)
    season = models.ForeignKey('Season',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.id) +'  '+ self.name
class League(models.Model):#hecho
    id = models.IntegerField(primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=50, null=True)
    link = models.CharField(max_length=50, null=True)
    abbreviation = models.CharField(max_length=10, null=True)
    hasWildCard = models.BooleanField(null=True)
    hasSplitSeason = models.BooleanField(null=True)
    numGames = models.IntegerField(null=True)
    hasPlayoffPoints = models.BooleanField(null=True)
    numTeams = models.IntegerField(null=True)
    numWildcardTeams = models.IntegerField(null=True)
    season = models.ForeignKey('Season',on_delete=models.CASCADE,null=True)
    orgCode = models.CharField(max_length=10,null=True)
    conferencesInUse = models.BooleanField(null=True)
    divisionsInUse = models.BooleanField(null=True)
    sport = models.ForeignKey('Sport',on_delete=models.CASCADE,null=True)
    sortOrder = models.IntegerField(null=True)
    active = models.BooleanField(null=True)
    nameShort = models.CharField(max_length=50,null=True)
    seasonState = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.id) +'  '+ self.name
class Division(models.Model):#hecho
    id = models.IntegerField(primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=50, null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, null=True)
    nameShort = models.CharField(max_length=50, null=True)
    link = models.CharField(max_length=50, null=True)
    abbreviation = models.CharField(max_length=10, null=True)
    league = models.ForeignKey('League', on_delete=models.CASCADE, null=True)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True)
    hasWildcard = models.BooleanField(null=True)
    sortOrder = models.IntegerField(null=True)
    numPlayoffTeams = models.IntegerField(null=True)
    active = models.BooleanField(null=True)

    def __str__(self):
        return str(self.id) +'  '+ self.name
class Sport(models.Model):#hecho
    id = models.IntegerField(primary_key=True, unique=True, blank=False)
    code = models.CharField(max_length=10,null=True)
    link = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    abbreviation = models.CharField(max_length=10, null=True)
    sortOrder = models.IntegerField(null=True)
    activeStatus = models.BooleanField(null=True)
    def __str__(self):
        if type(self.name) == type('') :
            aux = str(self.id) + '-->' + self.name
        else :
            aux = str(self.id)
        return aux
class Season(models.Model):#hecho
    seasonId = models.IntegerField(primary_key=True, blank=False)
    sportId = models.ManyToManyField('Sport',through='SeasonSportDate')
    def __str__(self):
        return str(self.seasonId)
    class SeasonSportDate(models.Model):
        seasonId = models.ForeignKey('Season',on_delete=models.CASCADE,blank=True,null=True)
        sportId = models.ForeignKey('Sport',on_delete=models.CASCADE,blank=True,null=True)
        hasWildcard = models.BooleanField(null=True)
        preSeasonStartDate = models.DateField(null=type)
        preSeasonEndDate = models.DateField(null=type)
        seasonStartDate = models.DateField(null=type)
        springStartDate = models.DateField(null=type)
        springEndDate = models.DateField(null=type)
        regularSeasonStartDate = models.DateField(null=type)
        lastDate1stHalf = models.DateField(null=type)
        allStarDate = models.DateField(null=type)
        firstDate2ndHalf = models.DateField(null=type)
        regularSeasonEndDate = models.DateField(null=type)
        postSeasonStartDate = models.DateField(null=type)
        postSeasonEndDate = models.DateField(null=type)
        seasonEndDate = models.DateField(null=type)
        offseasonStartDate = models.DateField(null=type)
        offSeasonEndDate = models.DateField(null=type)
        seasonLevelGamedayType = models.CharField(max_length=1, null=type)
        gameLevelGamedayType = models.CharField(max_length=1, null=type)
        qualifierPlateAppearances = models.FloatField(null=True)
        qualifierOutsPitched = models.FloatField(null=True)

        def __str__(self):
            return str(self.seasonId) + '-->' + str(self.sportId)

class Player(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, blank=False)
    team = models.ManyToManyField('Teams', null=True)
    primaryPosition = models.ForeignKey('Position', on_delete=models.CASCADE, null=True)
    fullName = models.CharField(max_length=50,null=True)
    link = models.CharField(max_length=50,null=True)
    firstName = models.CharField(max_length=50,null=True)
    lastName = models.CharField(max_length=50,null=True)
    birthDate = models.CharField(max_length=50,null=True)
    currentAge = models.IntegerField(null=True)
    birthCity = models.CharField(max_length=50,null=True)
    birthStateProvince = models.CharField(max_length=50,null=True)
    birthCountry = models.CharField(max_length=50,null=True)
    height = models.CharField(max_length=50,null=True)
    weight = models.IntegerField(null=True)
    active = models.BooleanField(null=True)
    primaryNumber = models.CharField(max_length=3,null=True)
    useName = models.CharField(max_length=50,null=True)
    useLastName = models.CharField(max_length=50,null=True)
    middleName = models.CharField(max_length=50,null=True)
    boxscoreName = models.CharField(max_length=50,null=True)
    nickName = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=1,null=True)
    nameMatrilineal = models.CharField(max_length=50,null=True)
    isPlayer = models.BooleanField(null=True)
    isVerified = models.BooleanField(null=True)
    draftYear = models.CharField(max_length=50,null=True)
    deathDate = models.CharField(max_length=50,null=True)
    deathCity = models.CharField(max_length=50,null=True)
    deathStateProvince = models.CharField(max_length=50,null=True)
    deathCountry = models.CharField(max_length=50,null=True)
    lastPlayedDate = models.CharField(max_length=50,null=True)
    pronunciation = models.CharField(max_length=50,null=True)
    mlbDebutDate = models.CharField(max_length=50,null=True)
    batSide = models.CharField(max_length=1,null=True)
    pitchHand = models.CharField(max_length=1,null=True)
    nameFirstLast = models.CharField(max_length=50,null=True)
    nameTitle = models.CharField(max_length=50,null=True)
    namePrefix = models.CharField(max_length=50, null=True)
    nameSuffix = models.CharField(max_length=50,null=True)
    nameSlug = models.CharField(max_length=50,null=True)
    firstLastName = models.CharField(max_length=50,null=True)
    lastFirstName = models.CharField(max_length=50,null=True)
    lastInitName = models.CharField(max_length=50,null=True)
    initLastName = models.CharField(max_length=50,null=True)
    fullFMLName = models.CharField(max_length=100,null=True)
    fullLFMName = models.CharField(max_length=100,null=True)
    strikeZoneTop = models.FloatField(null=True)
    strikeZoneBottom = models.FloatField(null=True)
    def __str__(self):
        return str(self.id)
class Position(models.Model):#hecho
    shortName = models.TextField(max_length=50, null=True)
    fullName = models.TextField(max_length=50, null=True)
    abbrev = models.TextField(max_length=10,null=True)
    code = models.TextField(primary_key=True, unique=True, blank=False)
    type = models.TextField(max_length=50, null=True)
    formalName = models.TextField(max_length=50, null=True)
    displayName = models.TextField(max_length=50, null=True)
    pitcher = models.BooleanField(null=True)
    gamePosition = models.BooleanField(null=True)
    fielder = models.BooleanField(null=True)
    outfield = models.BooleanField(null=True)
    def __str__(self):
        return self.fullName
class Roster(models.Model):
    person =  models.ForeignKey('Player',on_delete=models.CASCADE,null=True)
    jerseyNumber = models.TextField(max_length=5, null=True)
    position = models.ForeignKey('Position',on_delete=models.CASCADE,null=True)
    status = models.BooleanField(null=True)
    season = models.ForeignKey('Season',on_delete=models.CASCADE,null=True)


