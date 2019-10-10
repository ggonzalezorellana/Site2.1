from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Animal


def index(request):
    animales = Animal.objects.all()
    animals = []
    for animal in animales:
        animals.append({
                'nro': animal.nro,
                'name': animal.name,
                'color': animal.color,
                'nacimiento': animal.birth,
                'etapa': animal.stage
            }
        )

    title = 'Animales actuales'
    cal = animals
    head = 'Site1/App1'
    
    return render(request, 'App1/index.html', {'head': head, 'title': title, 'cal': cal})


def profile(request, nro):
    animal = Animal.objects.filter(nro=nro)[0]

    ani_mal = {'nro': animal.nro,
                'name': animal.name,
                'color': animal.color,
                'nacimiento': animal.birth,
                'etapa': animal.stage
               }

    head = animal.name
    title = 'Perfil %s'%animal.name
    cal = [ani_mal]

    return render(request, 'App1/index.html', {'head': head, 'title': title, 'cal': cal})
