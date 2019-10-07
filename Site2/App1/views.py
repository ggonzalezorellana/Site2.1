from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal


def index(request):
    animales = Animal.objects.all()
    for animal in animales:
        print(animal.nro, animal.name)
    return HttpResponse("Hello, world. You're at the App1 index.")