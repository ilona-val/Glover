from django.contrib.auth.models import User
from django.db.models import Q

from .models import Profile, Like, Match

 
def get_discover_profiles(profile: Profile):
    """ When given a profile, this function returns all to-be-discovered profiles that match both the 
        given profile's "looking for" choice, as well as reverse matching the "looking for" field for
        potential matches to ensure they match the given profile's gender 
    """
    likes = Like.objects.filter(profile=profile)
    looking_for = profile.looking_for
    gender = profile.gender
    already_liked = [l.profile_liked for l in likes]
    users = User.objects.exclude(Q(profile__in=already_liked) | Q(profile=profile)).select_related('profile')
    users = users.filter(profile__gender=looking_for)

    # remove users who are not looking for the given user's gender
    users = [user for user in users if user.profile.looking_for == gender]
    return users

def get_matches(profile: Profile):
    """ Gets all matches for the user """
    matches = Match.objects.filter(Q(profile1=profile) | Q(profile2=profile))
    profiles = []
    for match in matches:
        if match.profile1.pk != profile.pk:
            profiles.append(match.profile1)
        else:
            profiles.append(match.profile2)
    return profiles

def num_recent_matches(profile: Profile):
    """ Gets the number of new matches for a user since they last logged in """
    last_login = profile.user.last_login 

    if last_login is not None:
        matches =  Match.objects.filter(Q(profile1=profile) | Q(profile2=profile)) \
                                .filter(time_matched__gt=last_login)
        return matches.count()
    return 0