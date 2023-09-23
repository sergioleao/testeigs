from rest_framework import viewsets
from  employer.api.serializers import EmployeeSerializer
from employer.models import Employee
from rest_framework import  permissions

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class EmployeeListViewset(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [permissions.AllowAny]