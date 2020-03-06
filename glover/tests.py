from django.test import TestCase


class ProfileTests(TestCase):
    # test get_matches
    # test that when two users like each other, a Match is created
    # test that when a user unlikes a user they've matched with, the Match object is removed
    # if user blocks another user, then get rid of match and check the Like object's "is_liked" field is set to false
    #
    pass