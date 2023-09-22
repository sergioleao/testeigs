from rest_framework import viewsets
from  employer.api.serializers import EmployeeSerializer
from employer.models import Employee


class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()