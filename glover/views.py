from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from glover.forms import UserRegistrationForm, LoginForm
from glover.models import Profile, Match, Like

 
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
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            dob = user_form.cleaned_data['dob']
            gender = user_form.cleaned_data['gender']
            profile = Profile.objects.create(user=user, dob=dob, gender=gender)

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
    #user = User.objects.get(username=request.user)
    #profile = Profile.objects.get(user=user)

    profile_list = Profile.objects.order_by('user__username')[:10]

    context_dict = {}
    context_dict['profiles'] = profile_list

    return render(request, 'glover/discover.html', context=context_dict)


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
def profile(request):
    profile = request.user.profile

    return render(request, 'glover/profile.html', {"profile": profile})


@login_required
def matches(request):
    context_dict = {}

    try:
        user_profile = request.user.profile
        matches = user_profile.get_matches()
        context_dict['Matches'] = matches

    except Match.DoesNotExist:
        context_dict['Matches'] = None

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

    return render(request, 'glover/like.html', context=context_dict)


