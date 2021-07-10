from django.shortcuts import render
from django.http import HttpResponse
import random


def home(req):
    return render(req, 'generator/home.html')


def password(req):
    symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j',
               'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    spec = ['`', '!', '@', '#', '$', '%', '^', '&', '*',
            '(', ')', '_', '+', '-', '=', '.', '<', '>', ',', '/', '?', '|', '~']
    symbol += letters

    if req.GET.get('upper'):
        symbol = symbol + list(map(lambda i: i.upper(), letters))

    if req.GET.get('spec'):
        symbol += spec

    x = ''

    for i in range(int(req.GET.get('length', 8))):
        x += symbol[random.randrange(0, len(symbol)-1)]

    return render(req, 'generator/home.html', {'pass': x})
