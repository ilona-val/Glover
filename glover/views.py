from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from glover.forms import UserForm, UserProfileForm
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
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'glover/register.html',
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered})


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
	profile_list = Profile.objects.order_by('username')[:10]

	context_dict = {}
	context_dict['profiles'] = profile_list

	return render(request, 'glover/discover.html', context=context_dict)


def discover_profile(request, username):
	context_dict = {}

	try:
		profile = Profile.objects.get(username=username)

		context_dict['profile'] = profile

	except Profile.DoesNotExist:
		context_dict['profile'] = None

	return render(request, 'glover/profile.html', context=context_dict)   
