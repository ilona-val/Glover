from django.contrib import admin

from glover.models import Like, Match

# Register your models here.
class LikeAdmin(admin.ModelAdmin):
	list_display = ('profile', 'profile_liked', 'is_liked')


class MatchAdmin(admin.ModelAdmin):
	list_display = ('profile1', 'profile2', 'time_matched')



admin.site.register(Like, LikeAdmin)
admin.site.register(Match, MatchAdmin)