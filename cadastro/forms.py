from django import forms
from .models import Animal, Vaccine


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['sex', 'age', 'ear_tag_number', 'mother_ear_tag_number']


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'application_date', 'second_dose', 'second_dose_date']

    def clean(self):
        cleaned_data = super().clean()
        second_dose = cleaned_data.get('second_dose')
        second_dose_date = cleaned_data.get('second_dose_date')
        if second_dose and not second_dose_date:
            self.add_error('second_dose_date', 'Informe a data da segunda dose')
        if not second_dose:
            cleaned_data['second_dose_date'] = None
        return cleaned_data
