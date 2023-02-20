from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('azertyuiopqsdfghjklmwxcvbn')
    if request.GET.get('uppercase'):
        characters.extend('AZERTYUIOPQSDFGHJKLMWXCVBN')

    if request.GET.get('numbers', ''):
        characters.extend('0123456789')

    if request.GET.get('special', ''):
        characters.extend('=+@#&%*$€£')

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})



# git stash is to remove what u've done lately


