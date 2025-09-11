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

    def age_components(self, reference_date=None):
        if not self.birth_date:
            return None, None
        today = reference_date or date.today()
        years = today.year - self.birth_date.year
        months = today.month - self.birth_date.month
        if today.day < self.birth_date.day:
            months -= 1
        if months < 0:
            years -= 1
            months += 12
        return years, months

    @property
    def age_display(self):
        years, months = self.age_components()
        if years is None:
            return ''
        parts = []
        if years:
            parts.append(f"{years} ano{'s' if years != 1 else ''}")
        if months:
            parts.append(f"{months} mês{'es' if months != 1 else ''}")
        if not parts:
            parts.append('0 meses')
        return ' '.join(parts)

    def save(self, *args, **kwargs):
        if self.birth_date:
            years, _ = self.age_components()
            self.age = years
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


class Weighing(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='weighings', verbose_name='animal'
    )
    weigh_date = models.DateField('data de pesagem')
    weight = models.FloatField('peso (kg)')
    age_years = models.PositiveIntegerField('idade (anos)', blank=True, null=True)
    age_months = models.PositiveIntegerField('idade (meses)', blank=True, null=True)

    def save(self, *args, **kwargs):
        years, months = self.animal.age_components(reference_date=self.weigh_date)
        self.age_years = years
        self.age_months = months
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.animal} - {self.weigh_date}"
