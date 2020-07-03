from django.contrib import admin
from .models import FreeLeague,MegaLeague,HotLeague,Winners,FreeLeagueChat

# Register your models here.
admin.site.register(FreeLeague)
admin.site.register(MegaLeague)
admin.site.register(HotLeague)

admin.site.register(Winners)
admin.site.register(FreeLeagueChat)