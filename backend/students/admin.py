from django.contrib import admin
from .models import Student, Gatepass, DayScholar, Hostelite

models_list = [Student, Gatepass, DayScholar, Hostelite]
admin.site.register(models_list)
