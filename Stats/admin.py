from django.contrib import admin
from Stats.models import *

# Register your models here.

admin.site.register(Teams)
admin.site.register(Sport)
admin.site.register(Division)
admin.site.register(League)
admin.site.register(Season)
admin.site.register(Venue)
admin.site.register(Position)
admin.site.register(Player)
admin.site.register(Roster)
admin.site.register(Season.SeasonSportDate)

