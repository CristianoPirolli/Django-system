from django.db import migrations, models


def clean_weights(apps, schema_editor):
    Animal = apps.get_model('cadastro', 'Animal')
    for animal in Animal.objects.all():
        w = animal.weight
        if isinstance(w, str):
            if w.strip() == "":
                animal.weight = None
            else:
                try:
                    animal.weight = float(w.replace(',', '.'))
                except ValueError:
                    animal.weight = None
            animal.save(update_fields=['weight'])


class Migration(migrations.Migration):
    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='weight',
            field=models.FloatField('peso (kg)', blank=True, null=True),
        ),
        migrations.RunPython(clean_weights, reverse_code=migrations.RunPython.noop),
    ]
