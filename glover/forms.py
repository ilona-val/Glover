from django import forms
from glover.models import Profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)


# haven't included course/interests/societies bc for some reason 
# they are not populated in the register form 
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('username', 'dob', 'gender', 'bio', 'year_in', 'location', 
			'library_floor', 'looking_for', )