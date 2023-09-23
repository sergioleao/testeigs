from rest_framework import serializers
from employer.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')
    class Meta:
        model = Employee
        fields = "__all__"