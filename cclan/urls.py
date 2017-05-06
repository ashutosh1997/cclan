"""cclan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

import home
import login
import signup
import user_account
from cclan import settings
from home import views
from login import views
from signup import views
from user_account import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('home.urls')),
    url(r'^about_us/', home.views.about_us, name='about_us'),

    url(r'^signup/', signup.views.signup, name='signup'),
    url(r'^showdata/', signup.views.showdata, name='showdata'),

    url(r'^user/auth/$', login.views.auth_view),
    url(r'^login/$', login.views.login, name='login'),
    url(r'^logout/$', user_account.views.logout, name='logout'),

    url(r'^user_account/$', user_account.views.my_account, name='my_account'),
    url(r'^update_avatar/', user_account.views.update_avatar, name='update_avatar'),
    url(r'^update_profile/', user_account.views.update_profile, name='update_profile'),
    url(r'^create_post/', user_account.views.create_post, name='create_post'),
    url(r'^delete_post/', user_account.views.delete_post, name='delete_post'),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ]
