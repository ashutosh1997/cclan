from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

from signup.forms import SignupForm, ProfileForm, ProfilePicForm
from signup.models import UserProfile


def signup(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user_account')
    else:
        user_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')

        if request.method == 'POST' and user_form.is_valid() \
                and username_present(username) is False \
                and email_present(email) is False:
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            # if profile_form.is_valid():
            profile_form.save()

            image_form = ProfilePicForm(request.POST, request.FILES)
            if image_form.is_valid():
                m = UserProfile.objects.get(pk=user.id)
                m.avatar = image_form.cleaned_data['avatar']
                m.save()
                return HttpResponse('image upload success')

            # return render(request, 'signup_success.html', {'uname': username, 'email': email})
            return HttpResponseRedirect('/user_account/')

        elif request.method == 'POST' and username_present(username) is True:
            return render(request, 'username_error.html', {'uname': username})

        elif request.method == 'POST' and email_present(email) is True:
            return render(request, 'email_error.html', {'email': email})

        else:
            signup_active = "active"
            return render(request, 'signin.html', {'signup_active': signup_active})


def showdata(request):
    all_users = User.objects.all()
    profiles = UserProfile.objects.all()
    return render(request, 'showdata.html', {'all_users': all_users, 'profiles': profiles})


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


def email_present(email):
    if User.objects.filter(email=email).exists():
        return True
    return False
