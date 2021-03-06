
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main/home.html",{'message':'Hi, there!'})#main-ul din templates


def formular(request):
    return render(request, "main/formular.html")

def formular_submit(request):
    return render(request, "main/raspunsformular.html",{'name':request.POST['nume'],'prenume':request.POST['prenume'],'trimite':request.POST['trimite']})
# Create your views here.

from .forms import PersonForm
from .models import Person

def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            person = Person()
            person.nume = cd['nume']
            person.mail = cd['email']
            person.phonenumber = cd['phonenumber']
            person.save()
            form = PersonForm()
        else:
            print("Form is not valid")
    else:
        form = PersonForm()

    return render(request, 'main/contact_form.html', {'form': form})


def persons(request):
    if request.method == 'GET':
        persons = Person.objects.all()

    return render(request, 'main/persons.html', {'persons': persons}) #randeaza din nou pagina html


def deleteperson(request, id): #aici paseaza id-ul primit in url
    if request.method == 'GET':
        Person.objects.all().filter(pk = int(id)).delete() #filtrez dupa primary key
        persons = Person.objects.all()

    return render(request, 'main/persons.html', {'persons': persons})