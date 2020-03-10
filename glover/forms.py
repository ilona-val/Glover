from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from glover.choices import GenderChoices
from glover.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        user_name = self.cleaned_data['username']
        pw = self.cleaned_data['password']

        # check the user exists
        if not User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("This user does not exist.")

        # check if user is active, return custom message if not
        if not User.objects.get(username=user_name).is_active:
            raise forms.ValidationError("This user's profile is disabled.")
        
        # check user's authentication details are correct
        if not authenticate(username=user_name, password=pw):
            raise forms.ValidationError("Invalid login details.")

        return self.cleaned_data



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=GenderChoices.get_choices(), widget=forms.Select(), required=True)

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
        
    