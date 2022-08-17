
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')

def user(request):
    return render(request, 'user_profile.html')


