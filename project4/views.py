from django.shortcuts import render, get_object_or_404
from django.views import generic, View


def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
