from django.contrib import admin
from .models import Animal, Vaccine, Weighing

admin.site.register(Animal)
admin.site.register(Vaccine)
admin.site.register(Weighing)
