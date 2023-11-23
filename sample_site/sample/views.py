from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import EmployeeRoster

# Create your views here.
# def home(request):
#     template = loader.get_template("myhome.html")
#     return HttpResponse(template.render())

def home(request):
    myEmployees = EmployeeRoster.objects.all().values()
    template = loader.get_template("myhome.html")
    context = {
        "Employees":myEmployees
    }
    return HttpResponse(template.render(context, request))
    
