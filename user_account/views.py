from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from signup.models import UserProfile
from user_account.forms import ProfileUpdateForm, ProfilePicUpdateForm, PostForm, CoverPicUpdateForm
from user_account.models import Post


def my_account(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.get(pk=user.id)
        all_posts = Post.objects.all().order_by("-timestamp")
        context = {
            'user': user,
            'profile': profile,
            'all_posts': all_posts
        }
        return render_to_response('profile.html', context)
    else:
        return HttpResponseRedirect('/login/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
    # return render_to_response('logout.html')


@csrf_exempt
def update_avatar(request):
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(pk=user.id)
    user = request.user
    if request.user.is_authenticated:
        image_form = ProfilePicUpdateForm(request.POST, request.FILES)
        if request.method == 'POST' and image_form.is_valid():
            m = UserProfile.objects.get(pk=user.id)
            m.avatar = image_form.cleaned_data['avatar']
            m.save()

        return HttpResponseRedirect('/user_account/')

    return HttpResponseRedirect('/login/')


@csrf_exempt
def update_cover(request):
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(pk=user.id)
    user = request.user
    if request.user.is_authenticated:
        cover_form = CoverPicUpdateForm(request.POST, request.FILES)
        if request.method == 'POST' and cover_form.is_valid():
            m = UserProfile.objects.get(pk=user.id)
            m.cover = cover_form.cleaned_data['cover']
            m.save()

        return HttpResponseRedirect('/user_account/')

    return HttpResponseRedirect('/login/')


@csrf_exempt
def update_profile(request):
    # c = {}
    # c.update(csrf(request))
    if request.user.is_authenticated:

        if request.method == 'POST':
            profile_update_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
            profile_update_form.save()
            return HttpResponseRedirect('/user_account/')

        else:
            return HttpResponseRedirect('/user_account/')

    return HttpResponseRedirect('/login/')


@csrf_exempt
def create_post(request):
    if request.user.is_authenticated:
        # post_form = PostForm(request.POST or None, request.FILES or None)
        #
        # if request.method == 'POST' and post_form.is_valid():
        #     instance = post_form.save(commit=False)
        #     instance.save()

        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

        return HttpResponseRedirect('/user_account/')

    return HttpResponseRedirect('/login/')


def delete_post(request):
    return HttpResponse("<h1>Functionality coming soon...</h1>")


