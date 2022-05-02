from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def booking(request):
    return render(request, 'booking.html')
