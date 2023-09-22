from django.contrib import admin

from employer.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Employee, EmployeeAdmin)
