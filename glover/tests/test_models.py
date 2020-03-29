from django.test import TestCase

from glover.models import *
from glover.utils import get_discover_profiles
from .test_helpers import populate


class ProfileTests(TestCase):
    # test get_matches
    # test that when two users like each other, a Match is created
    # test that when a user unlikes a user they've matched with, the Match object is removed
    # if user blocks another user, then get rid of match and check the Like object's "is_liked" field is set to false
    
    def setUp(self):
        # create users/profiles
        populate()

    def test_get_discover_profiles(self):
        """ Tests the utils.get_discover_profiles method returns correct profiles """
        jessica = Profile.objects.get(user__username='jessica')
        discovery_profiles = get_discover_profiles(jessica) # call the function
        self.assertEqual(len(discovery_profiles), 3)

        # create a new like and a new dislike to ensure the profiles are removed from the discovery list
        Like.objects.create(profile=jessica, profile_liked=discovery_profiles[0].profile, is_liked=True)
        self.assertEqual(len(get_discover_profiles(jessica)), 2)
        Like.objects.create(profile=jessica, profile_liked=discovery_profiles[1].profile, is_liked=False)
        self.assertEqual(len(get_discover_profiles(jessica)), 1)

        # change existing user's gender and preference to ensure function updates correctly
        greta = Profile.objects.get(user__username='greta')
        greta.gender = 'M'
        greta.looking_for = 'F'
        greta.save()
        self.assertEqual(len(get_discover_profiles(jessica)), 2)

        # test another user
        bob = Profile.objects.get(user__username='bob')
        discovery_profiles = get_discover_profiles(bob)
        self.assertEqual(len(discovery_profiles), 1)

        # change gender of match to ensure it is removed
        discovery_profiles[0].profile.gender = 'F'
        discovery_profiles[0].profile.save()
        discovery_profiles = get_discover_profiles(bob)
        self.assertEqual(len(discovery_profiles), 0)