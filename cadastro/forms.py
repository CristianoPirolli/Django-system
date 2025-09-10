from django import forms
from .models import Animal, Vaccine


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['sex', 'age', 'ear_tag_number', 'mother_ear_tag_number', 'birth_date', 'weight', 'weigh_date']
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.HiddenInput(),
            'ear_tag_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_ear_tag_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'weigh_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'sex': 'Sexo',
            'ear_tag_number': 'Nº do brinco',
            'mother_ear_tag_number': 'Nº do brinco da mãe',
            'birth_date': 'Data de nascimento',
            'weight': 'Peso (kg)',
            'weigh_date': 'Data da pesagem',
        }

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is None:
            return weight
        try:
            return float(str(weight).replace(',', '.'))
        except (TypeError, ValueError):
            raise forms.ValidationError('Informe um número válido para o peso')


VACCINE_CHOICES = [
    ('Aftosa', 'Aftosa'),
    ('Brucelose', 'Brucelose'),
    ('Raiva', 'Raiva'),
    ('Carbúnculo', 'Carbúnculo'),
    ('Clostridiose', 'Clostridiose'),
    ('Leptospirose', 'Leptospirose'),
    ('IBR/IPV', 'IBR/IPV'),
    ('BVD', 'BVD'),
    ('Botulismo', 'Botulismo'),
]


class VaccineForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=VACCINE_CHOICES,
        label='Nome da vacina',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Vaccine
        fields = ['name', 'application_date', 'second_dose', 'second_dose_date']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'second_dose': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'second_dose_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
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
