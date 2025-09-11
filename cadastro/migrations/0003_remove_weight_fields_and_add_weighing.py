from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_alter_animal_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='weigh_date',
        ),
        migrations.CreateModel(
            name='Weighing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weigh_date', models.DateField('data de pesagem')),
                ('weight', models.FloatField('peso (kg)')),
                ('age_years', models.PositiveIntegerField('idade (anos)', blank=True, null=True)),
                ('age_months', models.PositiveIntegerField('idade (meses)', blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=models.CASCADE, related_name='weighings', to='cadastro.animal', verbose_name='animal')),
            ],
        ),
    ]
