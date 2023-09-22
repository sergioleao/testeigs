from rest_framework import viewsets
from department.api.serializers import DepartmentSerializer
from department.models import Department


class DepartamentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()