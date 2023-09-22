from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


    def __str__(self) -> str:
        if type(self.name) == str:
            return self.name
        else:
            return "Error Name Department"