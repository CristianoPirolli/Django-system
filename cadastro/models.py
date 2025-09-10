from django.db import models
from django.core.exceptions import ValidationError


class Animal(models.Model):
    SEX_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    ear_tag_number = models.CharField(max_length=50)
    mother_ear_tag_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ear_tag_number} ({self.get_sex_display()})"


class Vaccine(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    application_date = models.DateField()
    second_dose = models.BooleanField(default=False)
    second_dose_date = models.DateField(blank=True, null=True)

    def clean(self):
        if self.second_dose and not self.second_dose_date:
            raise ValidationError('Informe a data da segunda dose.')
        if not self.second_dose:
            self.second_dose_date = None

    def __str__(self):
        return f"{self.name} - {self.animal}"
