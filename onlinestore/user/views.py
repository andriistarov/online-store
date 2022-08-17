from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def user_profile(request, username):
    context = {
        'username': username,
        'name': "Dmitro Dmitrov"
    }
    return render(request, 'user_profile.html', context)
