from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField('sexo', max_length=1, choices=[('M', 'Macho'), ('F', 'Fêmea')])),
                ('age', models.PositiveIntegerField('idade', blank=True, null=True)),
                ('ear_tag_number', models.CharField('nº do brinco', max_length=50)),
                ('mother_ear_tag_number', models.CharField('nº do brinco da mãe', max_length=50)),
                ('birth_date', models.DateField('data de nascimento', blank=True, null=True)),
                ('weight', models.DecimalField('peso (kg)', max_digits=6, decimal_places=2, blank=True, null=True)),
                ('weigh_date', models.DateField('data de pesagem', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField('nome', max_length=100)),
                ('application_date', models.DateField('data de aplicação')),
                ('second_dose', models.BooleanField('segunda dose', default=False)),
                ('second_dose_date', models.DateField('data da segunda dose', blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=models.CASCADE, to='cadastro.animal', verbose_name='animal')),
            ],
        ),
    ]
