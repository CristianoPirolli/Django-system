from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Animal(models.Model):
    SEX_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    sex = models.CharField('sexo', max_length=1, choices=SEX_CHOICES)
    age = models.PositiveIntegerField('idade', blank=True, null=True)
    ear_tag_number = models.CharField('nº do brinco', max_length=50)
    mother_ear_tag_number = models.CharField('nº do brinco da mãe', max_length=50)
    birth_date = models.DateField('data de nascimento', blank=True, null=True)

    def __str__(self):
        return f"{self.ear_tag_number} ({self.get_sex_display()})"

    def save(self, *args, **kwargs):
        if self.birth_date:
            today = date.today()
            self.age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        super().save(*args, **kwargs)


class Vaccine(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='animal')
    name = models.CharField('nome', max_length=100)
    application_date = models.DateField('data de aplicação')
    second_dose = models.BooleanField('segunda dose', default=False)
    second_dose_date = models.DateField('data da segunda dose', blank=True, null=True)

    def clean(self):
        if self.second_dose and not self.second_dose_date:
            raise ValidationError('Informe a data da segunda dose.')
        if not self.second_dose:
            self.second_dose_date = None

    def __str__(self):
        return f"{self.name} - {self.animal}"
