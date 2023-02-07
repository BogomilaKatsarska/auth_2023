from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic as views
from django.shortcuts import render

from django.contrib.auth.models import User


def index(request):
    print(
        authenticate(username='doncho', password='2343aish!#'),
        authenticate(username='bogomilak', password='b04ko123!@'),
    )
    '''
    # new_user = User.objects.create_user(
    #     username='bogomilak',
    #     password='b04ko123!@',
    #     first_name='Bogomila',
    #     last_name='Katsarska',
    # )
    # print(request.user)
    '''
    user_message = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f'The user is {user_message}authenticated')


# The User Methods Examples:
'''
get_username() - returns the username for the user(use this method instead of 
referencing the username attribute directly
get_full_name() - returns '{first_name} {last_name}'
get_short_name() - returns first_name only
'''


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Bogomila',
        password='123!*&BOJNnjsa',
    )

    login(request, user)


# FBV
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse(f'You are {request.user.username}')


class ProfileView(LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f'You are {request.user.username}')
