from django.contrib.auth.models import User
from django.db import models

#
# GENDER = (
#     ('male', 'MALE'),
#     ('female', 'FEMALE'),
#     ('other', 'OTHER'),
# )


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pic/user', default='profile_pic/user/default.png',
                               blank=True)
    gender = models.CharField(max_length=6)
    bio = models.CharField(max_length=500, null=True, blank=True)
    qualification = models.CharField(max_length=50, null=True, blank=True)
    college = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, blank=True)
    hometown = models.CharField(max_length=50, null=True, blank=True)
    rel_status = models.CharField(max_length=25, null=True, blank=True)
    dob = models.DateField(null=False, default='1997-01-01')

    def __str__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


# from django.db import models
#
#
# # Create your models here.
#
#
# class User(models.Model):
#     username = models.CharField(max_length=100, primary_key=True)
#     first_name = models.CharField(max_length=100, default='')
#     last_name = models.CharField(max_length=100, default='')
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#
#     # this returns the name of the user when the object of user is printed
#     def __str__(self):
#         return self.username
#

