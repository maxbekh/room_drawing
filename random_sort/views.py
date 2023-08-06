from django.shortcuts import render
from .models import Person, Chamber
import random

def index(request):
    Chamber.objects.all().delete()
    Person.objects.all().delete()
    return render(request, 'index.html')

def draw_results(request):
    # Check if people and chambers exist, if not, create them
    if not Person.objects.exists():
        Person.objects.create(name='Maxence Agra')
        Person.objects.create(name='Maxence Bouch')
        Person.objects.create(name='Maxence Bek')

    people = list(Person.objects.all())
    random.shuffle(people)

    if not Chamber.objects.exists():
        Chamber.objects.create(name='Chambre Miroir', picture='chamber_pictures/mirror.jpg', person=people[0])
        Chamber.objects.create(name='Chambre Arbre', picture='chamber_pictures/tree.jpg', person=people[1])
        Chamber.objects.create(name='Chambre Porte', picture='chamber_pictures/door.jpg', person=people[2])

    
    chambers = list(Chamber.objects.all())

    

    chambers_def = Chamber.objects.all()
    return render(request, 'draw_results.html', {'chambers': chambers_def})
