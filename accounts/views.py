"""
Server-rendered pages for accounts. All actual authentication happens
through the JSON API in accounts/api/ - these views just serve the
HTML shell that the frontend JavaScript operates on.
"""
from django.shortcuts import render


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')
