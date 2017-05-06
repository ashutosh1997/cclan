from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

from signup.models import UserProfile


class SignupForm(UserCreationForm):
    # username = forms.CharField(label='Username', required=True,
    #                            widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    #
    # first_name = forms.CharField(label='First name', required=True,
    #                              widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    #
    # last_name = forms.CharField(label='Last name', required=False,
    #                             widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    #
    # email = forms.EmailField(label='Email', required=True,
    #                          widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))
    #
    # password1 = forms.CharField(label='Password (minimum 8 characters)', required=True,
    #                             widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    #
    # password2 = forms.CharField(label='Confirm Password', required=True,
    #                             widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


# GENDER = (
#     ('male', 'MALE'),
#     ('female', 'FEMALE'),
#     ('other', 'OTHER'),
# )


class ProfileForm(forms.ModelForm):
    # gender = forms.ChoiceField(choices=GENDER, required=True)
    # bio = forms.CharField(label='Bio',required=True,
    #                       widget=forms.TextInput(attrs={'placeholder': 'Enter Bio'}))
    #
    # location = forms.CharField(label='Location',required=True,
    #                            widget=forms.TextInput(attrs={'placeholder': 'Enter location'}))
    #
    # dob = fields.DateField(label='DOB', required=True,
    #                        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ('gender', 'bio', 'location', 'dob')


class ProfilePicForm(forms.ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ('avatar', )

