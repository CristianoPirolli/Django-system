from django.shortcuts import get_object_or_404, redirect, render
from .models import Animal, Vaccine
from .forms import AnimalForm, VaccineForm


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})


def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm()
    return render(request, 'animal_form.html', {'form': form, 'is_edit': False})


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    vaccines = animal.vaccine_set.all()
    return render(request, 'animal_detail.html', {'animal': animal, 'vaccines': vaccines})


def vaccine_create(request, animal_pk):
    animal = get_object_or_404(Animal, pk=animal_pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            vaccine = form.save(commit=False)
            vaccine.animal = animal
            vaccine.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = VaccineForm()
    return render(request, 'vaccine_form.html', {'form': form, 'animal': animal, 'is_edit': False})


def vaccine_edit(request, animal_pk, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk, animal_id=animal_pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('animal_detail', pk=animal_pk)
    else:
        form = VaccineForm(instance=vaccine)
    return render(request, 'vaccine_form.html', {'form': form, 'animal': vaccine.animal, 'is_edit': True})


def vaccine_delete(request, animal_pk, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk, animal_id=animal_pk)
    if request.method == 'POST':
        vaccine.delete()
        return redirect('animal_detail', pk=animal_pk)
    return render(request, 'vaccine_confirm_delete.html', {'vaccine': vaccine})


def animal_edit(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animal_form.html', {'form': form, 'animal': animal, 'is_edit': True})


def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_list')
    return render(request, 'animal_confirm_delete.html', {'animal': animal})
