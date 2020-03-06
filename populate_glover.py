import os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_team_B_project.settings')

import django
django.setup()

from glover.choices import *
from glover.models import *
from django.contrib.auth.models import User

def populate():

    add_societies()
    add_interests()
    add_courses()
    
    if User.objects.filter(username='ilona').exists():
        User.objects.all().delete()

    user1 = User.objects.create_user(username='tomas', password='1234', is_superuser=True, is_staff=True, email="tomas@student.gla.ac.uk", first_name="Tomas")
    user2 = User.objects.create_user(username='ilona', password='1234', is_superuser=True, is_staff=True, email="ilona@student.gla.ac.uk", first_name="Ilona")
    user3 = User.objects.create_user(username='vrinda', password='1234', is_superuser=True, is_staff=True, email="vrinda@student.gla.ac.uk", first_name="Vrinda")
    user4 = User.objects.create_user(username='fraser', password='1234', is_superuser=True, is_staff=True, email="fraser@student.gla.ac.uk", first_name="Fraser")
    user5 = User.objects.create_user(username='barbara', password='1234', is_superuser=True, is_staff=True, email="barbara@student.gla.ac.uk", first_name="Barbara")
    user6 = User.objects.create_user(username='bob', password='1234', email="bob@student.gla.ac.uk", first_name="Bob")
    user7 = User.objects.create_user(username='linda', password='1234', email="linda@student.gla.ac.uk", first_name="Linda")
    user8 = User.objects.create_user(username='jack', password='1234', email="jack@student.gla.ac.uk", first_name="Jack")
    user9 = User.objects.create_user(username='peter', password='1234', email="peter@student.gla.ac.uk", first_name="Peter")
    user10 = User.objects.create_user(username='melinda', password='1234', email="melinda@student.gla.ac.uk", first_name="Melinda")

    profiles = [
        {'user': user1, 'dob': '1996-05-16', 'gender': "M", 'bio': "sup it's Tomas", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 10},
        {'user': user2, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Ilona", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 10},
        {'user': user3, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Vrinda", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 10},            
        {'user': user4, 'dob': '1996-05-16', 'gender': "N", 'bio': "sup it's Fraser", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 10},
        {'user': user5, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Barbara", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 10},   
        {'user': user6, 'dob': '1996-05-16', 'gender': "N", 'bio': "sup it's Bob", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 26},
        {'user': user7, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Linda", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 26},
        {'user': user8, 'dob': '1996-05-16', 'gender': "M", 'bio': "sup it's Jack", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 2},            
        {'user': user9, 'dob': '1996-05-16', 'gender': "M", 'bio': "sup it's Peter", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 32},
        {'user': user10, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Melinda", 'year_in': 2, 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 26},            
    ]

    societies = Society.objects.all()
    interests = Interest.objects.all()

    for profile_data in profiles:
        p = add_profile(profile_data['user'], profile_data['dob'], profile_data['gender'], profile_data['bio'], profile_data['year_in'],
            profile_data['location'], profile_data['library_floor'], profile_data['looking_for'], profile_data['course_id'])
        
        p.societies.clear() # remove all existing societies from the user's profile
        p.interests.clear() # remove all existing interests from the user's profile
        
        # add profile's societies
        socs = []
        while len(socs) < 5:
            choice = random.choice(societies)
            if choice not in socs:
                socs.append(choice)
        p.societies.add(*socs)

        # add profile's interests
        intrs = []
        while len(intrs) < 5:
            choice = random.choice(interests)
            if choice not in intrs:
                intrs.append(choice)
        p.interests.add(*intrs)

    profiles = Profile.objects.all()

    for profile in profiles:
        for profile_liked in profiles:
            if not profile.pk == profile_liked.pk:
                like = add_like(profile, profile_liked)


def add_like(profile, profile_liked):
    like = Like.objects.get_or_create(profile=profile, profile_liked=profile_liked, is_liked=True)[0]
    
def add_profile(user, dob, gender, bio, year_in, location, library_floor, looking_for, course_id):
    profile = Profile.objects.get_or_create(user=user, dob=dob, gender=gender, bio=bio, year_in=year_in, 
            location=location, library_floor=library_floor, looking_for=looking_for, course_id=course_id)[0]
    return profile

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
    print('Starting GLover population script...', end="")
    populate()
    print('DONE')