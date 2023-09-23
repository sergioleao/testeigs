from django.db import models

from department.models import Department

# Create your models here.

class Employee(models.Model):
    """ Model Base of the employee class

    
    """
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if type(self.name) == str:
            return self.name
        else:
            return "Error Check Employer Name"

