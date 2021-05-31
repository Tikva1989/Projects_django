from django.shortcuts import redirect, render
from .models import Family, Animal, Person, Passport
from .forms import AnimalForm, FamilyForm, PersonForm, PassportForm
# Create your views here.

def all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'all_animals':animals})

def single_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'single_animal.html', {'animal': animal})

def single_family(request, family_id):
    fam = Family.objects.get(id=family_id)

    # animals = Animal.objects.filter(family=fam)
    animals = fam.animal_set.all()
    return render(request, 'single_family.html', {'family': fam, 'animals': animals})

def add_animal(request):
    if request.method == 'GET':
        return render(request, 'create_page.html',
         {'form': AnimalForm(), 'add_type':'Animal'})

    if request.method == 'POST':
        data = request.POST
        form = AnimalForm(data)
        if form.is_valid():
            print(form.cleaned_data)
            animal = Animal.objects.create(**form.cleaned_data)
        return redirect('all_animals')


def add_family(request):
    if request.method == 'GET':
        form = FamilyForm()
        return render(request, 'create_page.html', {'form':form, 'add_type':'Family'})

    if request.method == 'POST':
        form = FamilyForm(request.POST)
        
        if form.is_valid():
            fam = Family.objects.create(name=form.cleaned_data['name'])
        
        return redirect('single_family', fam.id)


def add_person(request):
    if request.method == 'GET':
        return render(request, 'create_page.html', {'form': PersonForm(), 'add_type':'Person'})
    
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(form.cleaned_data)
            Person.objects.create(**form.cleaned_data)
    return redirect('add_person')


def add_passport(request):
    if request.method == "GET":
        return render(request, 'create_page.html', {'form':PassportForm(), 'add_type':'Passport'})

    if request.method == "POST":
        form = PassportForm(request.POST)
        if form.is_valid():
            passport = Passport.objects.create(person=form.cleaned_data['person'], pass_id=form.cleaned_data['pass_id'])
            passport.visited_countries.set(form.cleaned_data['visited_countries'])

        return redirect('add_passport')


def person_details(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, 'person_details.html', {'person':person})