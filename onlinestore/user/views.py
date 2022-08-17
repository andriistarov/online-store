from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def user_profile(request):
    context = {}
    return render(request, 'user.html', context)

