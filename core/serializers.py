from rest_framework import serializers
from .models import Employee

# Defining our data representation
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']