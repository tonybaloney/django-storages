from django.shortcuts import render
from .models import Person
# Create your views here.

def home(request):
    persons = Person.objects.all()
    return render(request, 'home.html', {'people': persons})
