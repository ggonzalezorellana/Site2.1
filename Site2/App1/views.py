from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Animal


def index(request):
    animales = Animal.objects.all()
    animals = []
    for animal in animales:
        animals.append({
            animal.nro: {
                'name': animal.name,
                'color': animal.color,
                'nacimiento': animal.birth,
                'etapa': animal.stage}
            }
        )
    #return HttpResponse("Hello, world. You're at the App1 index.")
    return JsonResponse(animals, safe=False)