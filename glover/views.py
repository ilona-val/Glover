import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from glover.forms import UserRegistrationForm, LoginForm, EditProfileForm
from glover.models import Profile, Match, Like
from glover import utils

 
def index(request):
    context_dict = {}

    return render(request, 'glover/index.html', context=context_dict)


def about(request):
    context_dict = {}

    return render(request, 'glover/about.html', context=context_dict)


def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            dob = user_form.cleaned_data['dob']
            gender = user_form.cleaned_data['gender']
            profile = Profile.objects.create(user=user, dob=dob, gender=gender)

            login(request, user)
            return redirect(reverse('glover:discover'))
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()

    context = {
        'registration_form': user_form,
    }
    return render(request, 'glover/register.html', context)


def user_login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('glover:discover'))

    return render(request, 'glover/login.html', {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('glover:index'))


@login_required
def discover(request):
    profile = request.user.profile
    user_list = utils.get_discover_profiles(profile)
    profile_list = [u.profile for u in user_list]

    context_dict ={'profiles': profile_list}

    return render(request, 'glover/discover.html', context_dict)


@login_required
def discover_profile(request, username):
    context_dict = {}

    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        context_dict['profile'] = profile

    except Profile.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'glover/discover-profile.html', context=context_dict)

@login_required
def match_profile(request, username):
    context_dict = {}

    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        context_dict['profile'] = profile

    except Profile.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'glover/match-profile.html', context=context_dict)
    
########
# Profile Views

@login_required
def profile(request):
    profile = request.user.profile

    return render(request, 'glover/profile.html', {"profile": profile})


@login_required
def edit_profile(request):
    form = EditProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect(reverse('glover:profile'))

    return render(request, 'glover/edit-profile.html', {"form": form})

@login_required
def edit_photos(request):
    if request.method == 'POST':
        profile = request.user.profile
        picture_fields = [profile.image1, profile.image2, profile.image3, profile.image4, profile.image5]
        updatable_pics = [i for i in picture_fields if not bool(i)]
        update_field = ([bool(i) for i in picture_fields]).index(False) + 1 # get the number of the image-field to be updated

        if len(updatable_pics) > 0:
            img_file = request.FILES['file']
            updatable_pics[0].save(img_file.name, img_file, save=True)
            return JsonResponse({"imgnum": update_field, "imgpath": updatable_pics[0].url})
    return render(request, 'glover/edit-photos.html')


@login_required
def matches(request):
    context_dict = {}

    try:
        user_profile = request.user.profile
        matches = user_profile.get_matches()
        context_dict['matches'] = matches

    except Match.DoesNotExist:
        context_dict['matches'] = None

    return render(request, 'glover/matches.html', context=context_dict)


@login_required
def like(request, profile1, profile2):
    context_dict = {}

    try:
        user1 = User.objects.get(username=profile1)
        user2 = User.objects.get(username=profile2)

        profile1 = Profile.objects.get(user=user1)
        profile2 = Profile.objects.get(user=user2)

        if "like" in request.POST:
            like = Like.objects.get_or_create(profile=profile1, profile_liked=profile2, is_liked=True)[0]

        elif "dislike" in request.POST:
            like = Like.objects.get_or_create(profile=profile1, profile_liked=profile2, is_liked=False)[0]

        
        context_dict['like'] = like

    except Profile.DoesNotExist:
        context_dict['like'] = None

    return redirect(reverse('glover:discover'))


#### AJAX VIEWS
@login_required
def delete_photo(request):
    """ Deletes user picture specified by query parameter """
    picture = request.GET.get('img', None) # get the picture from the query parameter

    photo_profile_map = {
        "img1": request.user.profile.image1,
        "img2": request.user.profile.image2,
        "img3": request.user.profile.image3,
        "img4": request.user.profile.image4,
        "img5": request.user.profile.image5
    }

    if picture is None or picture not in photo_profile_map.keys():
        return redirect(reverse('glover:edit-photos'))

    photo_profile_map[picture].delete()

    picture_fields = list(photo_profile_map.values())

    if not bool(picture_fields[0]):
        for field in picture_fields[1:]:
            if bool(field):
                picture_fields[0].save(field.name, field)
                field.delete()
                request.user.profile.save()
                break

    return JsonResponse({"url": reverse('glover:edit-photos')})