from django import forms
from .models import Animal, Vaccine


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['sex', 'age', 'ear_tag_number', 'mother_ear_tag_number', 'birth_date']
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ear_tag_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_ear_tag_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'sex': 'Sexo',
            'age': 'Idade',
            'ear_tag_number': 'Nº do brinco',
            'mother_ear_tag_number': 'Nº do brinco da mãe',
            'birth_date': 'Data de nascimento',
        }


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'application_date', 'second_dose', 'second_dose_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'application_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'second_dose': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'second_dose_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome da vacina',
            'application_date': 'Data de aplicação',
            'second_dose': 'Segunda dose?',
            'second_dose_date': 'Data da segunda dose',
        }

    def clean(self):
        cleaned_data = super().clean()
        second_dose = cleaned_data.get('second_dose')
        second_dose_date = cleaned_data.get('second_dose_date')
        if second_dose and not second_dose_date:
            self.add_error('second_dose_date', 'Informe a data da segunda dose')
        if not second_dose:
            cleaned_data['second_dose_date'] = None
        return cleaned_data
