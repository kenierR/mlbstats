# Generated by Django 4.2.5 on 2023-10-19 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('nameShort', models.CharField(max_length=50, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('abbreviation', models.CharField(max_length=10, null=True)),
                ('hasWildcard', models.BooleanField(null=True)),
                ('sortOrder', models.IntegerField(null=True)),
                ('numPlayoffTeams', models.IntegerField(null=True)),
                ('active', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('abbreviation', models.CharField(max_length=10, null=True)),
                ('hasWildCard', models.BooleanField(null=True)),
                ('hasSplitSeason', models.BooleanField(null=True)),
                ('numGames', models.IntegerField(null=True)),
                ('hasPlayoffPoints', models.BooleanField(null=True)),
                ('numTeams', models.IntegerField(null=True)),
                ('numWildcardTeams', models.IntegerField(null=True)),
                ('orgCode', models.CharField(max_length=10, null=True)),
                ('conferencesInUse', models.BooleanField(null=True)),
                ('divisionsInUse', models.BooleanField(null=True)),
                ('sortOrder', models.IntegerField(null=True)),
                ('active', models.BooleanField(null=True)),
                ('nameShort', models.CharField(max_length=50, null=True)),
                ('seasonState', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fullName', models.CharField(max_length=50, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('firstName', models.CharField(max_length=50, null=True)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('birthDate', models.CharField(max_length=50, null=True)),
                ('currentAge', models.IntegerField(null=True)),
                ('birthCity', models.CharField(max_length=50, null=True)),
                ('birthStateProvince', models.CharField(max_length=50, null=True)),
                ('birthCountry', models.CharField(max_length=50, null=True)),
                ('height', models.CharField(max_length=50, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('active', models.BooleanField(null=True)),
                ('primaryNumber', models.CharField(max_length=3, null=True)),
                ('useName', models.CharField(max_length=50, null=True)),
                ('useLastName', models.CharField(max_length=50, null=True)),
                ('middleName', models.CharField(max_length=50, null=True)),
                ('boxscoreName', models.CharField(max_length=50, null=True)),
                ('nickName', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('nameMatrilineal', models.CharField(max_length=50, null=True)),
                ('isPlayer', models.BooleanField(null=True)),
                ('isVerified', models.BooleanField(null=True)),
                ('draftYear', models.CharField(max_length=50, null=True)),
                ('deathDate', models.CharField(max_length=50, null=True)),
                ('deathCity', models.CharField(max_length=50, null=True)),
                ('deathStateProvince', models.CharField(max_length=50, null=True)),
                ('deathCountry', models.CharField(max_length=50, null=True)),
                ('lastPlayedDate', models.CharField(max_length=50, null=True)),
                ('pronunciation', models.CharField(max_length=50, null=True)),
                ('mlbDebutDate', models.CharField(max_length=50, null=True)),
                ('batSide', models.CharField(max_length=1, null=True)),
                ('pitchHand', models.CharField(max_length=1, null=True)),
                ('nameFirstLast', models.CharField(max_length=50, null=True)),
                ('nameTitle', models.CharField(max_length=50, null=True)),
                ('namePrefix', models.CharField(max_length=50, null=True)),
                ('nameSuffix', models.CharField(max_length=50, null=True)),
                ('nameSlug', models.CharField(max_length=50, null=True)),
                ('firstLastName', models.CharField(max_length=50, null=True)),
                ('lastFirstName', models.CharField(max_length=50, null=True)),
                ('lastInitName', models.CharField(max_length=50, null=True)),
                ('initLastName', models.CharField(max_length=50, null=True)),
                ('fullFMLName', models.CharField(max_length=100, null=True)),
                ('fullLFMName', models.CharField(max_length=100, null=True)),
                ('strikeZoneTop', models.FloatField(null=True)),
                ('strikeZoneBottom', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('shortName', models.TextField(max_length=50, null=True)),
                ('fullName', models.TextField(max_length=50, null=True)),
                ('abbrev', models.TextField(max_length=10, null=True)),
                ('code', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('type', models.TextField(max_length=50, null=True)),
                ('formalName', models.TextField(max_length=50, null=True)),
                ('displayName', models.TextField(max_length=50, null=True)),
                ('pitcher', models.BooleanField(null=True)),
                ('gamePosition', models.BooleanField(null=True)),
                ('fielder', models.BooleanField(null=True)),
                ('outfield', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('seasonId', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=10, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('abbreviation', models.CharField(max_length=10, null=True)),
                ('sortOrder', models.IntegerField(null=True)),
                ('activeStatus', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=55, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(null=True)),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.season')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('allStarStatus', models.CharField(max_length=1, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('teamCode', models.CharField(max_length=10, null=True)),
                ('fileCode', models.CharField(max_length=10, null=True)),
                ('abbreviation', models.CharField(max_length=10, null=True)),
                ('teamName', models.CharField(max_length=50, null=True)),
                ('locationName', models.CharField(max_length=50, null=True)),
                ('firstYearOfPlay', models.CharField(max_length=4, null=True)),
                ('shortName', models.CharField(max_length=50, null=True)),
                ('parentOrgName', models.CharField(max_length=50, null=True)),
                ('parentOrgId', models.IntegerField(null=True)),
                ('franchiseName', models.CharField(max_length=50, null=True)),
                ('clubName', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(null=True)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.division')),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.league')),
                ('season', models.ManyToManyField(null=True, to='Stats.season')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.sport')),
                ('springLeague', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='springLeague', to='Stats.league')),
                ('springVenue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='springVenue', to='Stats.venue')),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.venue')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonSportDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasWildcard', models.BooleanField(null=True)),
                ('preSeasonStartDate', models.DateField(null=type)),
                ('preSeasonEndDate', models.DateField(null=type)),
                ('seasonStartDate', models.DateField(null=type)),
                ('springStartDate', models.DateField(null=type)),
                ('springEndDate', models.DateField(null=type)),
                ('regularSeasonStartDate', models.DateField(null=type)),
                ('lastDate1stHalf', models.DateField(null=type)),
                ('allStarDate', models.DateField(null=type)),
                ('firstDate2ndHalf', models.DateField(null=type)),
                ('regularSeasonEndDate', models.DateField(null=type)),
                ('postSeasonStartDate', models.DateField(null=type)),
                ('postSeasonEndDate', models.DateField(null=type)),
                ('seasonEndDate', models.DateField(null=type)),
                ('offseasonStartDate', models.DateField(null=type)),
                ('offSeasonEndDate', models.DateField(null=type)),
                ('seasonLevelGamedayType', models.CharField(max_length=1, null=type)),
                ('gameLevelGamedayType', models.CharField(max_length=1, null=type)),
                ('qualifierPlateAppearances', models.FloatField(null=True)),
                ('qualifierOutsPitched', models.FloatField(null=True)),
                ('seasonId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.season')),
                ('sportId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.sport')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='sportId',
            field=models.ManyToManyField(through='Stats.SeasonSportDate', to='Stats.sport'),
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jerseyNumber', models.TextField(max_length=5, null=True)),
                ('status', models.BooleanField(null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.player')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.position')),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.season')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='primaryPosition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.position'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ManyToManyField(null=True, to='Stats.teams'),
        ),
        migrations.AddField(
            model_name='league',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.season'),
        ),
        migrations.AddField(
            model_name='league',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.sport'),
        ),
        migrations.AddField(
            model_name='division',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.league'),
        ),
        migrations.AddField(
            model_name='division',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.season'),
        ),
        migrations.AddField(
            model_name='division',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.sport'),
        ),
    ]
