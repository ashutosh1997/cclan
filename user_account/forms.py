from django import forms
from django.forms import fields, ModelForm
from signup.models import UserProfile
from user_account.models import Post


class ProfileUpdateForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ('gender', 'bio', 'qualification', 'college', 'location', 'hometown', 'rel_status', 'dob')


class ProfilePicUpdateForm(ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ('avatar',)


class CoverPicUpdateForm(ModelForm):
    cover = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ('cover',)


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('post_text', 'post_image', )
