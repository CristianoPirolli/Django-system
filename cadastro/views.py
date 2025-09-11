from django.shortcuts import get_object_or_404, redirect, render
from .models import Animal, Vaccine, Weighing
from .forms import AnimalForm, VaccineForm, WeighingForm


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
    weights = animal.weighings.all()
    return render(
        request,
        'animal_detail.html',
        {'animal': animal, 'vaccines': vaccines, 'weights': weights},
    )


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


def weighing_create(request, animal_pk):
    animal = get_object_or_404(Animal, pk=animal_pk)
    if request.method == 'POST':
        form = WeighingForm(request.POST)
        if form.is_valid():
            weighing = form.save(commit=False)
            weighing.animal = animal
            weighing.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = WeighingForm()
    return render(
        request,
        'weighing_form.html',
        {'form': form, 'animal': animal, 'is_edit': False},
    )


def weighing_edit(request, animal_pk, pk):
    weighing = get_object_or_404(Weighing, pk=pk, animal_id=animal_pk)
    if request.method == 'POST':
        form = WeighingForm(request.POST, instance=weighing)
        if form.is_valid():
            form.save()
            return redirect('animal_detail', pk=animal_pk)
    else:
        form = WeighingForm(instance=weighing)
    return render(
        request,
        'weighing_form.html',
        {'form': form, 'animal': weighing.animal, 'is_edit': True},
    )


def weighing_delete(request, animal_pk, pk):
    weighing = get_object_or_404(Weighing, pk=pk, animal_id=animal_pk)
    if request.method == 'POST':
        weighing.delete()
        return redirect('animal_detail', pk=animal_pk)
    return render(request, 'weighing_confirm_delete.html', {'weighing': weighing})


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
