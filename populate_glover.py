import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_team_B_project.settings')

import django
django.setup()

from glover.choices import *
from glover.models import *
from django.contrib.auth.models import User

def populate():

    user1 = User.objects.create_user('tomas', password='1234')
    user1.save

    user2 = User.objects.create_user('ilona', password='1234')
    user2.save

    user3 = User.objects.create_user('vrinda', password='1234')
    user3.save

    user4 = User.objects.create_user('fraser', password='1234')
    user4.save

    user5 = User.objects.create_user('barbara', password='1234')
    user5.save

    profiles = {
        1: {'user': user1, 'username': 'tomas', 'id': user1.id, 'dob': '1995-01-05', 'gender': "M", 'bio': "sup it's Tomas", 
            'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "Female"},
        2: {'user': user2, 'username': 'ilona', 'id': user2.id,'dob': '1995-01-05', 'gender': "M", 'bio': "sup it's Ilona", 
            'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "Female"},
        3: {'user': user3, 'username': 'vrinda', 'id': user3.id,'dob': '1995-01-05', 'gender': "M", 'bio': "sup it's Vrinda", 
            'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "Female"},            
        4: {'user': user4, 'username': 'fraser', 'id': user4.id,'dob': '1995-01-05', 'gender': "M", 'bio': "sup it's Fraser", 
            'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "Female"},
        5: {'user': user5, 'username': 'barbara', 'id': user5.id,'dob': '1995-01-05', 'gender': "M", 'bio': "sup it's Barbara", 
            'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "Female"},            
    }


    for profile, profile_data in profiles.items():
        c = add_profile(profile_data['user'], profile_data['dob'], profile_data['gender'], profile_data['bio'], 
                profile_data['year_in'], profile_data['location'], profile_data['library_floor'], profile_data['looking_for'])


    # Print out the categories we have added.
    for c in Profile.objects.all():
        print(f'- {c}')

    add_societies()
    add_interests()
    add_courses()

def add_profile(user, dob, gender, bio, year_in, location, library_floor, looking_for):
    p = Profile.objects.get_or_create(user=user, dob=dob, gender=gender, 
        bio=bio, year_in=year_in, location=location, library_floor=library_floor, looking_for=looking_for)[0]
    p.save()
    return p

def add_societies():
    for society in SocietyChoices.ALL_CHOICES:
        Society.objects.get_or_create(society=society)

def add_interests():
    for interest in InterestChoices.ALL_CHOICES:
        Interest.objects.get_or_create(interest=interest)

def add_courses():
    for course in CourseChoices.ALL_CHOICES:
        Course.objects.get_or_create(course=course)


if __name__ == '__main__':
    print('Starting GLover population script...')
    populate()