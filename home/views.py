from django.shortcuts import render

from employer.models import Employee

# Create your views here.


def home(request):
    return render(request, 'index.html')

def listemploye(request):
    output = Employee.objects.all()
    return render(request, 'listemploye.html',{'output': output})

def listemployebyid(request, id):
    output = Employee.objects.filter(id)
    return render(request, 'listemploye.html',{'output': output})