from rest_framework import viewsets
from department.api.serializers import DepartmentSerializer
from department.models import Department
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions

class DepartamentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [permissions.IsAuthenticated]