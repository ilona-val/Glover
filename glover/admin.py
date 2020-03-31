from django.contrib import admin

from glover.models import Like, Match, Profile, Message


# Register your models here.
class LikeAdmin(admin.ModelAdmin):
    list_display = ('profile', 'profile_liked', 'is_liked')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('profile1', 'profile2', 'time_matched')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'gender',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message',)


admin.site.register(Like, LikeAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
