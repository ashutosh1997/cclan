from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


def login(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user_account')
    else:
        return render_to_response('signin.html', c)


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)

    if user and user.is_superuser:
        auth.logout(request)
        return HttpResponseRedirect('/login/')

    elif user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/user_account')

    else:
        return render_to_response('login_invalid.html')
        # return HttpResponseRedirect('/invalid')


#
# def loggedin(request):
#     if request.user.is_authenticated:
#         user = User.objects.get(id=request.user.id)
#         profile = UserProfile.objects.get(pk=user.id)
#         return render_to_response('my_account.html', {'user': user, 'profile': profile})
#     else:
#         return HttpResponseRedirect('/login')


# def invalid_login(request):
#     return render_to_response('login_invalid.html')


# def logout(request):
#     auth.logout(request)
#     return render_to_response('logout.html')
