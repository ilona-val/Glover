from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from glover.forms import UserRegistrationForm
from glover.models import Profile


def index(request):
    context_dict = {}

    return render(request, 'glover/index.html', context=context_dict)


def about(request):
    context_dict = {}

    return render(request, 'glover/about.html', context=context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            dob = user_form.cleaned_data['dob']
            gender = user_form.cleaned_data['gender']
            profile = Profile.objects.create(user=user, dob=dob, gender=gender)

            registered = True
            

            return redirect(reverse('glover:discover'))
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()

    context = {
        'registration_form': user_form,
        'registered': registered
    }
    return render(request, 'glover/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('glover:discover'))
            else:
                return HttpResponse("Your Glover account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'glover/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('glover:index'))


@login_required
def discover(request):
    profile_list = Profile.objects.order_by('user__username')[:10]

    context_dict = {}
    context_dict['profiles'] = profile_list

    return render(request, 'glover/discover.html', context=context_dict)


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