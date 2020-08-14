from django.contrib import admin
from .models import Employee

# Registering the model to manage via Django Admin
admin.site.register(Employee)