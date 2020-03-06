from django import forms
from django.contrib.auth.models import User

from glover.choices import GenderChoices
from glover.models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	first_name = forms.CharField(required=True)
	email = forms.CharField(required=True)
	dob = forms.DateField()
	gender = forms.ChoiceField(choices = GenderChoices.get_choices(), widget=forms.Select(), required=True)

	def clean_confirm_password(self):
		password1 = self.cleaned_data['password']
		password2 = self.cleaned_data['confirm_password']

		if not password1 == password2:
			raise forms.ValidationError("The passwords do not match.")
		return password2

	def clean_email(self):
		email = self.cleaned_data['email'].strip()

		if not email.endswith('@student.gla.ac.uk'):
			raise forms.ValidationError("Email must belong to a University of Glasgow account. ( @student.gla.ac.uk )")
		return email

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email', 'gender', 'dob', 'password', 'confirm_password')
